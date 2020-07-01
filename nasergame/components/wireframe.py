import pygame
from digicolor import colors

from nasergame.lib import math

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
        nodes = math.scale(nodes, self.scale)
        nodes = math.rotate(nodes, self.rotation)
        nodes = math.translate(nodes, self.translation)
        for startref, endref in self.model.lines:
            start = nodes[startref][:2]
            end = nodes[endref][:2]
            pygame.draw.line(screen, self.color, start, end)
