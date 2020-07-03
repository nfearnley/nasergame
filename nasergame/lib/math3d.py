import numpy as np
from . import matrix


def transform(a, b):
    return np.dot(a, b)


def combine(matrices):
    out = matrix.identity()
    for m in matrices:
        out = transform(out, m)
    return out


def project(nodes):
    w = nodes[:,3][:,None]
    return np.divide(nodes, w)
