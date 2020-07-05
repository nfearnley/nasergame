import numpy as np


from nasergame.lib.utils import fixedsplit


class ModelParseException(Exception):
    ...


def parse_vref(refstr):
    """Parse a vertex reference that may include unused references to other vertex types"""
    try:
        ref = int(refstr.split("/")[0])
    except ValueError:
        raise ModelParseException(f"Bad vertex reference: {ref}")
    return ref - 1


def parses(keyword):
    def wrapper(fn):
        fn._handles = keyword
        return fn
    return wrapper


def parser(cls):
    cls._handlers = {}
    for name, method in cls.__dict__.items():
        if hasattr(method, "_handles"):
            cls._handlers[method._handles] = method
    return cls


def map_vrefs(vrefs, nodes):
    out_nodes = np.zeros((0, 4))
    for vref in vrefs:
        node = nodes[vref]
        out_nodes = np.vstack((out_nodes, node))
    return out_nodes


@parser
class Model:
    def __init__(self, text):
        self.nodes = np.zeros((0, 4))
        self.vref_lines = []

        """load a wireframe from the contents of a Waveform OBJ model file"""

        # Remove line continuation characters "\"
        text = text.replace("\\\n", "")

        for text_line in text.splitlines():
            self.parse_line(text_line)

        self.lines = [map_vrefs(self.node, self.vref_lines)]

    def add_node(self, xyz):
        xyzw = np.hstack((xyz, 1))
        self.nodes = np.vstack((self.nodes, xyzw))

    def add_vref_line(self, line):
        self.vref_lines.append(line)

    def parse_text_line(self, text_line):
        """load a single line from a Waveform OBJ model file"""
        text_line = text_line.strip()
        if not text_line:
            # Ignore blank lines
            return
        if text_line.startswith("#"):
            # Ignore comment lines
            return

        keyword, args = fixedsplit(text_line, maxsplit=1)

        method = self._handlers.get(keyword)
        if not method:
            return
        method(self, args)

    @parses("v")
    def parse_vertex_element(self, args):
        try:
            coords = [float(a) for a in args.split()]
        except ValueError:
            coords = None
        if not (coords and 3 <= len(coords) <= 4):
            raise ModelParseException(f"Bad vector arguments: {args}")
        self.add_node(coords[:3])

    @parses("l")
    def parse_line_element(self, args):
        vrefs = [parse_vref(v) for v in args.split()]
        if len(vrefs) < 2:
            raise ModelParseException(f"Not enough vertex references in line: {args}")
        self.add_vref_line(vrefs)

    @parses("f")
    def parse_face_element(self, args):
        vrefs = [parse_vref(v) for v in args.split()]
        if len(vrefs) < 3:
            raise ModelParseException(f"Not enough vertex references in face: {args}")
        self.add_vref_line(vrefs + [vrefs[0]])
