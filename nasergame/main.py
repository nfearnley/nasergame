import math

import pygame
import pygame.gfxdraw
from pygame.locals import K_SPACE, K_q, K_w, K_e, K_a, K_s, K_d, K_LSHIFT, K_MINUS, K_EQUALS, K_r
from digicolor import colors

from nasergame import __version__
from nasergame import scaleddisplay
from nasergame.lib import models
from nasergame.components import Wireframe


def main():
    global toggle
    print(f"Welcome to NaserGame v{__version__}!")
    pygame.init()
    pygame.display.set_caption(f"NaserGame v{__version__}")

    framerate = 60
    screen = scaleddisplay.set_mode((512, 512), (512, 512))

    clock = pygame.time.Clock()

    #fighter = Wireframe(model=models.load("fighter1"))
    fighter = Wireframe(model=models.load("arwing_SNES"))
    fighter.scale = 250, 250, 250
    fighter.translation = 64, 64, 0

    scale_speed = 10
    translate_speed = 2
    rotate_speed = (math.pi * 2 / 360)

    running = True
    while running:
        # Close event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == K_r:
                fighter.scale = 1000, 1000, 1000
                fighter.rotation = 0, 0, 0
                fighter.translation = 256, 256, 0

        key_state = pygame.key.get_pressed()
        toggle = key_state[K_SPACE]
        if key_state[K_MINUS]:
            scale, _, _ = fighter.scale
            scale -= scale_speed
            fighter.scale = scale, scale, scale
        if key_state[K_EQUALS]:
            scale, _, _ = fighter.scale
            scale += scale_speed
            fighter.scale = scale, scale, scale
        if key_state[K_LSHIFT]:
            if key_state[K_w]:
                x, y, z = fighter.rotation
                x -= rotate_speed
                fighter.rotation = x, y, z
            if key_state[K_s]:
                x, y, z = fighter.rotation
                x += rotate_speed
                fighter.rotation = x, y, z
            if key_state[K_a]:
                x, y, z = fighter.rotation
                y -= rotate_speed
                fighter.rotation = x, y, z
            if key_state[K_d]:
                x, y, z = fighter.rotation
                y += rotate_speed
                fighter.rotation = x, y, z
            if key_state[K_q]:
                x, y, z = fighter.rotation
                z -= rotate_speed
                fighter.rotation = x, y, z
            if key_state[K_e]:
                x, y, z = fighter.rotation
                z += rotate_speed
                fighter.rotation = x, y, z
        else:
            if key_state[K_a]:
                x, y, z = fighter.translation
                x -= translate_speed
                fighter.translation = x, y, z
            if key_state[K_d]:
                x, y, z = fighter.translation
                x += translate_speed
                fighter.translation = x, y, z
            if key_state[K_w]:
                x, y, z = fighter.translation
                y -= translate_speed
                fighter.translation = x, y, z
            if key_state[K_s]:
                x, y, z = fighter.translation
                y += translate_speed
                fighter.translation = x, y, z
            if key_state[K_q]:
                x, y, z = fighter.translation
                z -= translate_speed
                fighter.translation = x, y, z
            if key_state[K_e]:
                x, y, z = fighter.translation
                z += translate_speed
                fighter.translation = x, y, z

        # UPDATE HERE

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # DRAW HERE

        fighter.render(screen)

        scaleddisplay.flip()

        # Timing loop
        clock.tick_busy_loop(framerate)


if __name__ == "__main__":
    main()
