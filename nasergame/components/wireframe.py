import pygame
from digicolor import colors
import numpy as np

from nasergame.lib import math3d as m3d

__all__ = ["Wireframe"]


def pairs(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return zip(iterable[::2], iterable[1::2])


def clip(line_nodes):
    clipped_nodes = []
    for n, f in pairs(line_nodes):
        if n[2] > f[2]:
            n, f = f, n
        if f[2] < 0:
            continue
        if n[2] < 0:
            xlen = f[0] - n[0]
            ylen = f[1] - n[1]
            zlen = f[2] - n[2]
            wlen = f[3] - n[3]
            visible = f[2] / zlen
            new_n = (
                f[0] - xlen * visible,
                f[1] - ylen * visible,
                0,
                f[3] - wlen * visible
            )
            clipped_nodes.extend((new_n, f))
        else:
            clipped_nodes.extend((n, f))
    return np.array(clipped_nodes)


class Wireframe():
    def __init__(self, model=None, color=colors.WHITE.rgb):
        self.model = model
        self.color = color
        self.scale = (1, 1, 1)
        self.rotation_matrix = m3d.matrix.identity()
        self.translation = (0, 0, 0)
        self.perspective_matrix = m3d.matrix.perspective(30, 0.5, 10)
        self.screen_matrix = m3d.matrix.NDCtoScreen(0, 512, 0, 512)

    def reset_rotation(self):
        self.rotation_matrix = m3d.matrix.identity()

    def rotate_world_x(self, rx):
        self.rotation_matrix = m3d.combine([self.rotation_matrix, m3d.matrix.rotateX(rx)])

    def rotate_world_y(self, ry):
        self.rotation_matrix = m3d.combine([self.rotation_matrix, m3d.matrix.rotateY(ry)])

    def rotate_world_z(self, rz):
        self.rotation_matrix = m3d.combine([self.rotation_matrix, m3d.matrix.rotateZ(rz)])

    def rotate_model_x(self, rx):
        self.rotation_matrix = m3d.combine([m3d.matrix.rotateX(rx), self.rotation_matrix])

    def rotate_model_y(self, ry):
        self.rotation_matrix = m3d.combine([m3d.matrix.rotateY(ry), self.rotation_matrix])

    def rotate_model_z(self, rz):
        self.rotation_matrix = m3d.combine([m3d.matrix.rotateZ(rz), self.rotation_matrix])

    def render(self, screen, toggle):
        line_nodes = self.model.line_nodes
        # model space -> world space
        matrix = m3d.combine([
            m3d.matrix.scale(self.scale),
            self.rotation_matrix,
            m3d.matrix.translate(self.translation),
            self.perspective_matrix
        ])
        line_nodes = m3d.transform(line_nodes, matrix)

        line_nodes = clip(line_nodes)
        # clip space -> viewport space
        line_nodes = m3d.project(line_nodes)
        # viewport space -> screen space
        line_nodes = m3d.transform(line_nodes, self.screen_matrix)
        pygame.draw.lines(screen, self.color, True, line_nodes[:,:2])
