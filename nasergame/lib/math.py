import numpy as np


def transform(nodes, matrix):
    return np.dot(nodes, matrix)


def translate(nodes, translation):
    return transform(nodes, translationMatrix(translation))


def translationMatrix(translation):
    """ Return matrix for translation along vector (dx, dy, dz). """
    dx, dy, dz = translation

    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [dx, dy, dz, 1]])


def scale(nodes, scale_factor):
    return transform(nodes, scaleMatrix(scale_factor))


def scaleMatrix(scale_factor):
    """ Return matrix for scaling equally along all axes centred on the point (cx,cy,cz). """
    sx, sy, sz = scale_factor

    return np.array([[sx, 0, 0, 0],
                     [0, sy, 0, 0],
                     [0, 0, sz, 0],
                     [0, 0, 0, 1]])


def rotate(nodes, rotation):
    rx, ry, rz = rotation
    nodes = rotateX(nodes, rx)
    nodes = rotateY(nodes, ry)
    nodes = rotateZ(nodes, rz)
    return nodes


def rotateX(nodes, rx):
    return transform(nodes, rotateXMatrix(rx))


def rotateXMatrix(rx):
    """ Return matrix for rotating about the x-axis by 'rx' radians """
    c = np.cos(rx)
    s = np.sin(rx)
    return np.array([[1, 0, 0, 0],
                     [0, c, -s, 0],
                     [0, s, c, 0],
                     [0, 0, 0, 1]])


def rotateY(nodes, ry):
    return transform(nodes, rotateYMatrix(ry))


def rotateYMatrix(ry):
    """ Return matrix for rotating about the y-axis by 'ry' radians """
    c = np.cos(ry)
    s = np.sin(ry)
    return np.array([[c, 0, s, 0],
                     [0, 1, 0, 0],
                     [-s, 0, c, 0],
                     [0, 0, 0, 1]])


def rotateZ(nodes, rz):
    return transform(nodes, rotateZMatrix(rz))


def rotateZMatrix(rz):
    """ Return matrix for rotating about the z-axis by 'rz' radians """
    c = np.cos(rz)
    s = np.sin(rz)
    return np.array([[c, -s, 0, 0],
                     [s, c, 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
