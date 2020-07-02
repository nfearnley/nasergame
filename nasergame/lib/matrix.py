import numpy as np

__all__ = ["translate", "scale", "rotateX", "rotateY", "rotateZ"]


def identity():
    """Identity matrix"""
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])


def translate(translation):
    """Matrix for translation along vector (dx, dy, dz)."""
    dx, dy, dz = translation

    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [dx, dy, dz, 1]])


def scale(scale_factor):
    """Matrix for scaling by (sx, sy, sz)."""
    sx, sy, sz = scale_factor

    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])


def rotateX(rx):
    """Matrix for rotating about the x-axis by rx radians"""
    c = np.cos(rx)
    s = np.sin(rx)
    return np.array([[1, 0, 0, 0],
                     [0, c, -s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])


def rotateY(ry):
    """Matrix for rotating about the y-axis by ry radians"""
    c = np.cos(ry)
    s = np.sin(ry)
    return np.array([[c, 0, s, 0],
                     [0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [0, 0, 0, 1]])


def rotateZ(rz):
    """Matrix for rotating about the z-axis by rz radians"""
    c = np.cos(rz)
    s = np.sin(rz)
    return np.array([[c, -s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])


# def projection(r, l, b, t, n, f):
#     # r = right, l = left, b = bottom, t = top, n = near, f = far

#     return np.array([[  2 * n / (r - l),                 0,                    0,  0],
#                      [                0,   2 * n / (t - b),                    0,  0],
#                      [(r + l) / (r - l), (t + b) / (t - b),   -(f + n) / (f - n), -1],
#                      [                0,                 0, -2 * f * n / (f - n),  0]])

# def projection(w, n, f):
#     # r = right, l = left, b = bottom, t = top, n = near, f = far
#     sxy = 2 * n / w

#     return np.array([[sxy,    0, 0, 0],
#                      [   0, sxy, 0, 0],
#                      [   0,   0, 0, 0],
#                      [   0,   0, 0, 1]])


def perspective():
    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 0, 0]])
