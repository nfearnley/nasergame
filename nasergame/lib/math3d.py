import numpy as np
from . import matrix


def transform(a, b):
    return np.dot(a, b)


def combine(matrices):
    out = matrix.identity()
    for m in matrices:
        out = transform(out, m)
    return out


def translate(nodes, translation):
    return transform(nodes, matrix.translate(translation))


def scale(nodes, scale_factor):
    return transform(nodes, matrix.scale(scale_factor))


def rotate(nodes, rotation):
    rx, ry, rz = rotation
    nodes = rotateX(nodes, rx)
    nodes = rotateY(nodes, ry)
    nodes = rotateZ(nodes, rz)
    return nodes


def rotateX(nodes, rx):
    return transform(nodes, matrix.rotateX(rx))


def rotateY(nodes, ry):
    return transform(nodes, matrix.rotateY(ry))


def rotateZ(nodes, rz):
    return transform(nodes, matrix.rotateZ(rz))


def project(nodes, r, l, b, t, n, f):
    return transform(nodes, matrix.projection(r, l, b, t, n, f))


def normalize(nodes):
    w = nodes[:,3][:,None]
    with np.errstate(divide="ignore"):
        return np.divide(nodes, w)