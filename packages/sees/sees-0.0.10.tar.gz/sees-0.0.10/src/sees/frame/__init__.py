import sys
from collections import defaultdict


import numpy as np
Array = np.ndarray
from scipy.linalg import block_diag

from sees.model  import FrameModel
from sees.state  import read_state, State, BasicState
from sees.config import Config, apply_config
from sees.canvas.canvas import LineStyle, NodeStyle


# Data shaping / Misc.
#----------------------------------------------------

# The following functions are used for reshaping data
# and carrying out other miscellaneous operations.

def _is_frame(el):
    return     "beam" in el["type"].lower() \
            or "dfrm" in el["type"].lower()


# Kinematics
#----------------------------------------------------

# The following functions implement various kinematic
# relations for standard frame models.

def elastic_curve(x: Array, v: list, L:float)->Array:
    "compute points along Euler's elastica"
    if len(v) == 2:
        ui, uj, (vi, vj) = 0.0, 0.0, v
    else:
        ui, vi, uj, vj = v
    xi = x/L                        # local coordinate
    N1 = 1.-3.*xi**2+2.*xi**3
    N2 = L*(xi-2.*xi**2+xi**3)
    N3 = 3.*xi**2-2*xi**3
    N4 = L*(xi**3-xi**2)
    y = ui*N1 + vi*N2 + uj*N3 + vj*N4
    return y.flatten()

def elastic_tangent(x: Array, v: list, L: float)->Array:
    if len(v) == 2:
        ui, uj, (vi, vj) = 0.0, 0.0, v
    else:
        ui, vi, uj, vj = v
    xi = x/L
    M3 = 1 - xi
    M4 = 6/L*(xi-xi**2)
    M5 = 1 - 4*xi+3*xi**2
    M6 = -2*xi + 3*xi**2
    return (ui*M3 + vi*M5 + uj*M4 + vj*M6).flatten()


def displaced_profile(
        coord: Array,
        displ: Array,        #: Displacements
        vect : Array = None, #: Element orientation vector
        Q = None,
        npoints: int = 10,
        tangent: bool = False
    ):
    n = npoints
    #           (------ndm------)
    reps = 4 if len(coord[0])==3 else 2

    # 3x3 rotation into local system
    # Q = rotation(coord, vect)
    # Local displacements
    u_local = block_diag(*[Q]*reps)@displ
    # Element length
    L = np.linalg.norm(coord[-1] - coord[0])

    # longitudinal, transverse, vertical, section, elevation, plan
    li, ti, vi, si, ei, pi = u_local[:6]
    lj, tj, vj, sj, ej, pj = u_local[6:]

    Lnew  = L + lj - li
    xaxis = np.linspace(0.0, Lnew, n)

    plan_curve = elastic_curve(xaxis, [ti, pi, tj, pj], Lnew)
    elev_curve = elastic_curve(xaxis, [vi,-ei, vj,-ej], Lnew)

    local_curve = np.stack([xaxis + li, plan_curve, elev_curve])

    if tangent:
        plan_tang = elastic_tangent(xaxis, [ti, pi, tj, pj], Lnew)
        elev_tang = elastic_tangent(xaxis, [vi,-ei, vj,-ej], Lnew)

        local_tang = np.stack([np.linspace(0,0,n), plan_tang, elev_tang])
        return (
            Q.T@local_curve + coord[0][None,:].T,
            Q.T@local_tang
        )

    return Q.T@local_curve + coord[0][None,:].T


class FrameArtist:
    ndm: int
    ndf: int
    model: "FrameModel"
    canvas: "Canvas"

    def __init__(self, model_data, response=None, ndf=None, loc=None, vert=2, **kwds):
        config = Config()
        if "config" in kwds:
            apply_config(kwds.pop("config"), config)

        apply_config(kwds, config)
        self.config = config

        canvas_type = config.get("canvas", "matplotlib")
        if not isinstance(canvas_type, str):
            self.canvas = canvas_type
        elif canvas_type == "matplotlib":
            import sees.canvas.mpl
            self.canvas = sees.canvas.mpl.MatplotlibCanvas(**config["canvas_config"])
        elif canvas_type == "femgl":
            import sees.canvas.femgl
            self.canvas = sees.canvas.femgl.FemGlCanvas(self.model, **config["canvas_config"])
        elif canvas_type == "plotly":
            import sees.canvas.ply
            self.canvas = sees.canvas.ply.PlotlyCanvas(**config["canvas_config"])
        elif canvas_type == "gltf":
            import sees.canvas.gltf
            self.canvas = sees.canvas.gltf.GltfLibCanvas(**config["canvas_config"])
        elif canvas_type == "trimesh":
            import sees.canvas.tri
            self.canvas = sees.canvas.tri.TrimeshCanvas(**config["canvas_config"])
        else:
            raise ValueError("Unknown canvas type " + str(canvas_type))

        self.canvas.config = config


        self.ndm = 3

        if ndf is None:
            ndf = 6

        elif ndf == 3:
            self.ndm = 2

        if vert == 3:
            R = np.eye(3)
        else:
            R = np.array(((1,0, 0),
                          (0,0,-1),
                          (0,1, 0)))

        self._plot_rotation = R

        self.model = model = FrameModel(model_data, shift=loc, rot=R,
                                        **kwds.get("model_config", {}))


        # Create permutation matrix
        if model.ndf == 2 and model.ndm == 2:
            self.dofs2plot = R@np.array(((1, 0),
                                         (0, 1),
                                         (0, 0)))

        elif ndf == 3 and model.ndm == 2:
            self.dofs2plot = block_diag(*[R]*2)@np.array(((1,0, 0),
                                                          (0,1, 0),
                                                          (0,0, 0),

                                                          (0,0, 0),
                                                          (0,0, 0),
                                                          (0,0, 1)))

        else:
            self.dofs2plot = block_diag(*[R]*2)

        self.displ_states = {}

    def add_point_displacements(self, displ, scale=1.0, name=None):
        displ_array = self.displ_states[name]
        for i,n in enumerate(self.model["nodes"]):
            for dof in displ[n]:
                displ_array[i, dof] = 1.0

        displ_array[:,3:] *= scale/100
        displ_array[:,:3] *= scale
        return name

    def _add_displ_case(self, state, name=None, scale=1.0):

        if name in self.displ_states:
            self.displ_states[name].update(state)
        else:
            self.displ_states[name] = state

        return name


    def add_state(self, res_file, scale=1.0, only=None, type=None):

        if not isinstance(res_file, (dict, Array, State)):
            state = read_state(res_file, only=only,
                               model=self.model,
                               scale=scale,
                               transform=self.dofs2plot)
        else:
            state = res_file

        # If dict of dicts, assume its a collection of responses, 
        # otherwise, just a single response
        if isinstance(state, dict) and isinstance(next(iter(state.values())), dict):
            for k, v in state.items():
                self._add_displ_case(v, name=k, scale=scale)

        elif isinstance(state, dict):
            self._add_displ_case(BasicState(state, self.model,
                                            scale=scale,
                                            transform=self.dofs2plot))

        else:
            self._add_displ_case(state, scale=scale)


    def plot_origin(self, **kwds):
        xyz = np.zeros((3,3))
        uvw = self._plot_rotation.T*kwds.get("scale", 1.0)
        off = [[0, -kwds.get("scale", 1.0)/2, 0],
               [0]*3,
               [0]*3]

        self.canvas.plot_vectors(xyz, uvw, **kwds)

        for i,label in enumerate(kwds.get("label", [])):
            self.canvas.annotate(label, (xyz+uvw)[i]+off[i])

    def add_elem_data(self):

        N = 3
        for type in self.model.cell_prototypes():
            name = type["name"]
            ni = len(type["instances"])
            coords = np.zeros((ni*(N+1),self.ndm))
            coords.fill(np.nan)
            for i,crd in enumerate(self.model.cell_position(type["instances"])):
                coords[(N+1)*i:(N+1)*i+N,:] = np.linspace(*crd, N)

            # coords = coords.reshape(-1,4,N)[:,-N]
            coords = coords.reshape(-1,4,3)[:,-3]

            self.canvas.plot_hover(coords, data=type["properties"],
                                   style=NodeStyle(shape="sphere"), label=name)



    def plot_chords(self, state=None, layer=None):
        model = self.model
        ndm   = self.model["ndm"]

        N = 2
        do_lines = False
        lines = np.zeros((len(model["assembly"])*(N+1),3))
        lines.fill(np.nan)

        triangles = []
        nodes = model.node_position(state=state)

        for i,(tag,el) in enumerate(model["assembly"].items()):
            position = model.cell_position(tag, state)[[0,-1],:]
            if _is_frame(el):
                do_lines = True
                lines[(N+1)*i:(N+1)*i+N,:] = position #np.linspace(el["crd"][0], el["crd"][-1], N)

            else:
                triangles.extend(model.cell_triangles(tag))

        if do_lines:
            self.canvas.plot_lines(lines[:,:self.ndm])


        if len(triangles) > 0:
            self.canvas.plot_mesh(nodes, np.array(triangles))

    def draw_edges(self, state=None, style=None):
        model = self.model
        ndm   = self.model["ndm"]

        N = 2
        do_lines = False
        lines = np.zeros((len(model["assembly"])*(N+1),3))
        lines.fill(np.nan)

        indices = []
        nodes = model.node_position(state=state)

        for i,(tag,el) in enumerate(model["assembly"].items()):
            position = model.cell_position(tag, state)[[0,-1],:]
            if _is_frame(el):
                do_lines = True
                lines[(N+1)*i:(N+1)*i+N,:] = position

            else:
                idx = model.cell_exterior(tag)
                indices.append([*idx, idx[0]])

        if do_lines:
            self.canvas.plot_lines(lines[:,:self.ndm], style=style)

        if len(indices) > 0:
            self.canvas.plot_lines(nodes, indices=np.array(indices), style=style)

    def draw_filled(self, state=None):
        from sees.frame import extrude
        return extrude.draw_extrusions(self.model,
                                       canvas=self.canvas,
                                       state=state,
                                       options=self.config)

        sections = get_section_geometries(self.model, self.config)

        # N = 2
        N = 20 if displ is not None else 2

        I = 0
        coords = []
        triang = []
        for i,el in enumerate(self.model["assembly"].values()):
            # if int(el["name"]) < 30: continue
            try:
                sect = sections[el["name"]]
            except:
                if int(el["name"]) < 1e3:
                    sect = self.config["default_section"]
                else:
                    sect = np.array([[-48, -48],
                                     [ 48, -48],
                                     [ 48,  48],
                                     [-48,  48]])



    def plot_displaced_assembly(self, state=None, label=None):
        model = self.model
        N  = 10 if state is not None else 2
        ne = len(model["assembly"])
        coords = np.zeros((ne*(N+1), 3))
        coords.fill(np.nan)

        do_lines = False
        for i,(tag,el) in enumerate(model["assembly"].items()):
            # exclude zero-length elements
            if _is_frame(el) and state is not None:
                do_lines = True
                glob_displ = state.cell_array(tag).flatten()
                vect = None #np.array(el["trsfm"]["vecInLocXZPlane"])[axes]
                coords[(N+1)*i:(N+1)*i+N,:] = displaced_profile(model.cell_position(tag),
                                                                glob_displ,
                                                                Q=model.frame_orientation(tag),
                                                                npoints=N).T
            elif len(el["crd"]) == 2:
                do_lines = True
                coords[(N+1)*i:(N+1)*i+N,:] = np.linspace(*el["crd"], N)

        if do_lines:
            self.canvas.plot_lines(coords[:, :self.ndm], style=LineStyle(color="red"), label=label)

    def plot_nodes(self, state=None, data=None, label=None):
        coord = self.model.node_position(state=state)
        self.canvas.plot_nodes(coord[:,:self.ndm], label=label)

        if state is None:
            self.canvas.plot_hover(coord[:,:self.ndm],
                                   label="node",
                                   keys=["tag", "crd"],
                                   data=[[str(k), list(map(str, coord[i]))]
                                       for i,k in enumerate(self.model.iter_node_tags())])

    def add_triads(self):
        ne = len(self.model["assembly"])
        xyz, uvw = np.nan*np.zeros((2, ne, 3, 3))

        for i,el in enumerate(self.model["assembly"].values()):
            axes = self.model.frame_orientation(el["name"])
            if axes is None:
                continue

            scale = np.linalg.norm(el["crd"][-1] - el["crd"][0])/10
            coord = sum(i for i in el["crd"])/len(el["nodes"])
            xyz[i,:,:] = np.array([coord]*3)
            uvw[i,:,:] = scale*axes

        self.canvas.plot_vectors(xyz.reshape(ne*3,3), uvw.reshape(ne*3,3))

    def draw(self):
        if "reference" in self.config["show_objects"] \
            or len(self.displ_states) == 0:

            self.plot_chords()
#           self.draw_edges()
            try:
                self.add_elem_data()
            except Exception as e:
#               raise e
                print(e, file=sys.stderr)

        if "nodes" in self.config["show_objects"]:
            self.plot_nodes()

        if "origin" in self.config["show_objects"]:
            self.plot_origin(**self.config["objects"]["origin"])

        if "triads" in self.config["show_objects"]:
            self.add_triads()

        for layer, state in self.displ_states.items():
            self.plot_nodes(state=state, label=layer)

            if "chords" in self.config["show_objects"]:
#               self.draw_edges(state=state) #, style=state.line_style)
                self.plot_chords(state=state, layer=layer)

            self.plot_displaced_assembly(state=state, label=layer)

        if "extrude" in self.config["show_objects"]:
            displ = None
            if len(self.displ_states) == 1:
                displ = next(iter(self.displ_states.values()))

            try:
                self.draw_filled(displ)
            except Exception as e:
                # raise e
                print("Warning -- ", e, file=sys.stderr)

        self.canvas.build()
        return self

    def save(self, filename):
        self.canvas.write(filename)

    def repl(self):
        from opensees.repl.__main__ import OpenSeesREPL
        self.canvas.plt.ion()

        try:
            from IPython import get_ipython
            get_ipython().run_magic_line('matplotlib')
        except:
            pass

        repl = OpenSeesREPL()

        def plot(*args):
            if len(args) == 0:
                return self.draw()

            elif hasattr(self, "plot_"+args[0]):
                return getattr(self, "plot_"+args[0])(*args[1:])

            elif hasattr(self, args[0]):
                return getattr(self, args[0])(*args[1:])

        repl.interp._interp.createcommand("plot", plot)
        # repl.interp._interp.createcommand("show", lambda *args: self.canvas.show())
        repl.repl()

