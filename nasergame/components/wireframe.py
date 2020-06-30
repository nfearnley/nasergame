import pygame
from digicolor import colors

from nasergame.lib import math

__all__ = ["Wireframe"]


def three_to_two(vertex, scale, offset):
    x, y, z, w = vertex
    x_scale, y_scale, z_scale = scale
    x_offset, y_offset, z_offset = scale
    new_x = (x * ((z * z_scale) + z_offset) * .3 * x_scale) + x_offset
    new_y = (y * ((z * z_scale) + z_offset) * .3 * y_scale) + y_offset
    return new_x, new_y


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
