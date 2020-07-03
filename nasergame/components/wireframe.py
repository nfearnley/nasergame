import pygame
from digicolor import colors
import numpy as np

from nasergame.lib import math3d as m3d

__all__ = ["Wireframe"]


def map_lines(lines, nodes):
    for startref, endref in lines:
        start = nodes[startref][:2]
        end = nodes[endref][:2]
        if np.any(np.isinf(start)) or np.any(np.isinf(end)):
            continue
        yield start, end


class Wireframe():
    def __init__(self, model=None, color=colors.WHITE.rgb):
        self.model = model
        self.color = color
        self.scale = (1, 1, 1)
        self.rotation_matrix = m3d.matrix.identity()
        self.translation = (0, 0, 0)

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
        nodes = self.model.nodes
        # model space -> world space
        matrix = m3d.combine([
            m3d.matrix.scale(self.scale),
            self.rotation_matrix,
            m3d.matrix.translate(self.translation),
        ])
        # world space -> view space
        ...
        #
        nodes = m3d.transform(nodes, matrix)
        # view space -> clip space
        # apply transformations        
        # TODO: Add clipping here
        lines = []
        near = 0.1
        for startref, endref in self.model.lines:
            start = nodes[startref]
            end = nodes[endref]
            if start[2] < near and end[2] < near:
                ...
            elif start[2] < near or end[2] < near:
                if end[2] < start[2]:
                    startref, endref = endref, startref
                    start, end = end, start
                diff = (near - start[2]) / (end[2] - start[2])
                newstart = (
                    (end[0] - start[0]) * diff + start[0],
                    (end[1] - start[1]) * diff + start[1],
                    near,
                    1
                )
                newstartref = len(nodes)
                nodes = np.vstack((nodes, newstart))
                lines.append((newstartref, endref))
            else:
                lines.append((startref, endref))

        # add perspective
        if toggle:
            nodes = m3d.transform(nodes, m3d.matrix.perspective(10))
        # clip space -> viewport space
        nodes = m3d.project(nodes)
        # viewport space -> screen space
        nodes = m3d.transform(nodes, m3d.matrix.NDCtoScreen(0, 512, 0, 512))
        # nodes = m3d.normalize(nodes)
        for start, end in map_lines(lines, nodes):
            pygame.draw.line(screen, self.color, start, end)
