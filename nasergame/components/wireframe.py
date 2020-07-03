from itertools import tee

import pygame
from digicolor import colors
import numpy as np

from nasergame.lib import math3d as m3d

__all__ = ["Wireframe"]


def pairs(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    return zip(iterable[::2], iterable[1::2])


class Wireframe():
    def __init__(self, model=None, color=colors.WHITE.rgb):
        self.model = model
        self.color = color
        self.scale = (1, 1, 1)
        self.rotation_matrix = m3d.matrix.identity()
        self.translation = (0, 0, 0)

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
        ])
        # world space -> view space
        ...
        #
        line_nodes = m3d.transform(line_nodes, matrix)
        # view space -> clip space
        # apply transformations
        # TODO: Add clipping here
        clipped_nodes = np.zeros((0,4))
        near = 0.1
        for start, end in pairs(line_nodes):
            if start[2] > end[2]:
                start, end = end, start
            if end[2] < near:
                continue
            if start[2] < near:
                diff = (near - start[2]) / (end[2] - start[2])
                newstart = (
                    (end[0] - start[0]) * diff + start[0],
                    (end[1] - start[1]) * diff + start[1],
                    near,
                    1
                )
                clipped_nodes = np.vstack((clipped_nodes, newstart))
                clipped_nodes = np.vstack((clipped_nodes, end))
            else:
                clipped_nodes = np.vstack((clipped_nodes, start))
                clipped_nodes = np.vstack((clipped_nodes, end))

        # add perspective
        if toggle:
            clipped_nodes = m3d.transform(clipped_nodes, m3d.matrix.perspective(10))
        # clip space -> viewport space
        clipped_nodes = m3d.project(clipped_nodes)
        # viewport space -> screen space
        clipped_nodes = m3d.transform(clipped_nodes, m3d.matrix.NDCtoScreen(0, 512, 0, 512))
        for start, end in pairs(clipped_nodes):
            pygame.draw.line(screen, self.color, start[:2], end[:2])
