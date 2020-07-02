import pygame
from digicolor import colors

from nasergame.lib import math3d as m3d

__all__ = ["Wireframe"]


class Wireframe():
    def __init__(self, model=None, color=colors.WHITE.rgb):
        self.model = model
        self.color = color
        self.scale = (1, 1, 1)
        self.rotation = (0, 0, 0)
        self.translation = (0, 0, 0)

    def render(self, screen):
        nodes = self.model.nodes
        matrix = m3d.combine([
            m3d.matrix.scale(self.scale),
            m3d.matrix.rotateX(self.rotation[0]),
            m3d.matrix.rotateY(self.rotation[1]),
            m3d.matrix.rotateZ(self.rotation[2]),
            m3d.matrix.translate(self.translation),
            m3d.matrix.perspective()
        ])
        nodes = m3d.transform(nodes, matrix)
        nodes = m3d.normalize(nodes)
        for startref, endref in self.model.lines:
            start = nodes[startref][:2]
            end = nodes[endref][:2]
            pygame.draw.line(screen, self.color, start, end)
