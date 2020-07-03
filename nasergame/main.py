import math

import pygame
import pygame.gfxdraw
from pygame.locals import K_q, K_w, K_e, K_a, K_s, K_d, K_LSHIFT, K_MINUS, K_EQUALS, K_LCTRL, K_SPACE
from digicolor import colors

from nasergame import __version__
from nasergame import scaleddisplay
from nasergame.lib import models
from nasergame.components import Wireframe


def main():
    print(f"Welcome to NaserGame v{__version__}!")
    pygame.init()
    pygame.display.set_caption(f"NaserGame v{__version__}")

    framerate = 60
    screen = scaleddisplay.set_mode((512, 512), (512, 512))

    clock = pygame.time.Clock()

    #fighter = Wireframe(model=models.load("fighter1"))
    #fighter = Wireframe(model=models.load("arwing_SNES"))
    fighter = Wireframe(model=models.load("cube"))
    fighter.scale = 0.5, 0.5, 0.5
    fighter.translation = 0, 0, 1
    fighter.rotate_world_y(math.radians(30))
    fighter.rotate_world_x(math.radians(15))

    scale_speed = 1
    translate_speed = 1
    rotate_speed = math.radians(60)

    toggled = False
    running = True
    while running:
        # Close event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                toggled = not toggled

        delay = clock.get_time()

        scale_amt = scale_speed * delay / 1000
        translate_amt = translate_speed * delay / 1000
        rotate_amt = rotate_speed * delay / 1000
        # Model manipulation
        key_state = pygame.key.get_pressed()

        if key_state[K_MINUS]:
            scale, _, _ = fighter.scale
            scale -= scale_amt
            fighter.scale = scale, scale, scale
        elif key_state[K_EQUALS]:
            scale, _, _ = fighter.scale
            scale += scale_amt
            fighter.scale = scale, scale, scale

        if key_state[K_LSHIFT]:
            if key_state[K_w]:
                fighter.rotate_world_x(-rotate_amt)
            if key_state[K_s]:
                fighter.rotate_world_x(rotate_amt)
            if key_state[K_a]:
                fighter.rotate_world_y(-rotate_amt)
            if key_state[K_d]:
                fighter.rotate_world_y(rotate_amt)
            if key_state[K_q]:
                fighter.rotate_world_z(-rotate_amt)
            if key_state[K_e]:
                fighter.rotate_world_z(rotate_amt)
        elif key_state[K_LCTRL]:
            if key_state[K_w]:
                fighter.rotate_model_x(-rotate_amt)
            if key_state[K_s]:
                fighter.rotate_model_x(rotate_amt)
            if key_state[K_a]:
                fighter.rotate_model_y(-rotate_amt)
            if key_state[K_d]:
                fighter.rotate_model_y(rotate_amt)
            if key_state[K_q]:
                fighter.rotate_model_z(-rotate_amt)
            if key_state[K_e]:
                fighter.rotate_model_z(rotate_amt)
        else:
            if key_state[K_a]:
                x, y, z = fighter.translation
                x -= translate_amt
                fighter.translation = x, y, z
            if key_state[K_d]:
                x, y, z = fighter.translation
                x += translate_amt
                fighter.translation = x, y, z
            if key_state[K_w]:
                x, y, z = fighter.translation
                y += translate_amt
                fighter.translation = x, y, z
            if key_state[K_s]:
                x, y, z = fighter.translation
                y -= translate_amt
                fighter.translation = x, y, z
            if key_state[K_q]:
                x, y, z = fighter.translation
                z -= translate_amt
                fighter.translation = x, y, z
            if key_state[K_e]:
                x, y, z = fighter.translation
                z += translate_amt
                fighter.translation = x, y, z

        # UPDATE HERE

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # DRAW HERE

        fighter.render(screen, toggled)

        scaleddisplay.flip()

        # Timing loop
        clock.tick_busy_loop(framerate)


if __name__ == "__main__":
    main()
