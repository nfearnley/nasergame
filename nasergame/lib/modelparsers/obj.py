import numpy as np


from nasergame.lib.utils import fixedsplit, pairs, wrapped_pairs


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


@parser
class Model:
    def __init__(self, text):
        self.nodes = np.zeros((0, 4))
        self.lines = []

        """load a wireframe from the contents of a Waveform OBJ model file"""

        # Remove line continuation characters "\"
        text = text.replace("\\\n", "")

        for line in text.splitlines():
            self.parse_line(line)

        # Remove an duplicate lines
        self.lines = list(dict.fromkeys(self.lines))
        self.line_nodes = np.array([self.nodes[ref] for line in self.lines for ref in line])

    def addNode(self, xyz):
        xyzw = np.hstack((xyz, 1))
        self.nodes = np.vstack((self.nodes, xyzw))

    def addLine(self, line):
        self.lines.append(line)

    def parse_line(self, line_text):
        """load a single line from a Waveform OBJ model file"""
        line_text = line_text.strip()
        if not line_text:
            # Ignore blank lines
            return
        if line_text.startswith("#"):
            # Ignore comment lines
            return

        keyword, args = fixedsplit(line_text, maxsplit=1)

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
        self.addNode(coords[:3])

    @parses("l")
    def parse_line_element(self, args):
        vrefs = [parse_vref(v) for v in args.split()]
        if len(vrefs) < 2:
            raise ModelParseException(f"Not enough vertex references in line: {args}")
        for refa, refb in pairs(vrefs):
            self.addLine((refa, refb))

    @parses("f")
    def parse_face_element(self, args):
        vrefs = [parse_vref(v) for v in args.split()]
        if len(vrefs) < 3:
            raise ModelParseException(f"Not enough vertex references in face: {args}")
        for refa, refb in wrapped_pairs(vrefs):
            self.addLine((refa, refb))
