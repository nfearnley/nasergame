import math

import pygame
import pygame.gfxdraw
from pygame.locals import K_q, K_w, K_e, K_a, K_s, K_d, K_f, K_LSHIFT, K_MINUS, K_EQUALS, K_LCTRL, K_SPACE
from digicolor import colors

from nasergame import __version__
from nasergame import scaleddisplay
from nasergame.lib import models
from nasergame.components import Wireframe


model_names = ["cube", "fighter1", "arwing_SNES"]
model_scales = [0.5, 5, 0.1]
selected_model = 0


def next_model(wf):
    global selected_model
    selected_model = (selected_model + 1) % len(model_names)
    load_model(wf)


def load_model(wf):
    model_name = model_names[selected_model]
    wf.model = models.load(model_name)
    wf.scale = (model_scales[selected_model],) * 3
    wf.translation = 0, 0, 1
    wf.reset_rotation()
    wf.rotate_world_y(math.radians(30))
    wf.rotate_world_x(math.radians(15))


def main():
    print(f"Welcome to NaserGame v{__version__}!")
    pygame.init()
    pygame.display.set_caption(f"NaserGame v{__version__}")

    framerate = 60
    screen = scaleddisplay.set_mode((512, 512), (512, 512))

    clock = pygame.time.Clock()

    #fighter = Wireframe(model=models.load("fighter1"))
    #fighter = Wireframe(model=models.load("arwing_SNES"))
    wf = Wireframe()
    load_model(wf)

    scale_speed = 1
    translate_speed = 1
    rotate_speed = math.radians(60)

    c = 0
    d = 4
    toggled = False
    running = True
    while running:
        # Close event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    toggled = not toggled
                elif event.key == K_f:
                    next_model(wf)
        delay = clock.get_time()

        scale_amt = scale_speed * delay / 1000
        translate_amt = translate_speed * delay / 1000
        rotate_amt = rotate_speed * delay / 1000
        # Model manipulation
        key_state = pygame.key.get_pressed()

        if key_state[K_MINUS]:
            scale, _, _ = wf.scale
            scale -= scale_amt
            wf.scale = scale, scale, scale
        elif key_state[K_EQUALS]:
            scale, _, _ = wf.scale
            scale += scale_amt
            wf.scale = scale, scale, scale

        if key_state[K_LSHIFT]:
            if key_state[K_w]:
                wf.rotate_world_x(-rotate_amt)
            if key_state[K_s]:
                wf.rotate_world_x(rotate_amt)
            if key_state[K_a]:
                wf.rotate_world_y(-rotate_amt)
            if key_state[K_d]:
                wf.rotate_world_y(rotate_amt)
            if key_state[K_q]:
                wf.rotate_world_z(-rotate_amt)
            if key_state[K_e]:
                wf.rotate_world_z(rotate_amt)
        elif key_state[K_LCTRL]:
            if key_state[K_w]:
                wf.rotate_model_x(-rotate_amt)
            if key_state[K_s]:
                wf.rotate_model_x(rotate_amt)
            if key_state[K_a]:
                wf.rotate_model_y(-rotate_amt)
            if key_state[K_d]:
                wf.rotate_model_y(rotate_amt)
            if key_state[K_q]:
                wf.rotate_model_z(-rotate_amt)
            if key_state[K_e]:
                wf.rotate_model_z(rotate_amt)
        else:
            if key_state[K_a]:
                x, y, z = wf.translation
                x -= translate_amt
                wf.translation = x, y, z
            if key_state[K_d]:
                x, y, z = wf.translation
                x += translate_amt
                wf.translation = x, y, z
            if key_state[K_w]:
                x, y, z = wf.translation
                y += translate_amt
                wf.translation = x, y, z
            if key_state[K_s]:
                x, y, z = wf.translation
                y -= translate_amt
                wf.translation = x, y, z
            if key_state[K_q]:
                x, y, z = wf.translation
                z -= translate_amt
                wf.translation = x, y, z
            if key_state[K_e]:
                x, y, z = wf.translation
                z += translate_amt
                wf.translation = x, y, z

        # UPDATE HERE

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # DRAW HERE

        wf.render(screen, toggled)
        c += d
        if c > 255:
            c = 255
            d = -d
        elif c < 0:
            c = 0
            d = -d
        screen.fill((c, 255 - c, 0), pygame.Rect(10, 10, 20, 20))
        scaleddisplay.flip()

        # Timing loop
        clock.tick_busy_loop(framerate)


if __name__ == "__main__":
    main()
