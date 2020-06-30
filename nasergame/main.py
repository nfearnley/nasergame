import pygame
from digicolor import colors

from nasergame import __version__
from nasergame import scaleddisplay


def main():
    print(f"Welcome to NaserGame v{__version__}!")
    pygame.init()
    pygame.display.set_caption(f"NaserGame v{__version__}")

    framerate = 60
    screen = scaleddisplay.set_mode((128, 128), (512, 512))

    clock = pygame.time.Clock()

    running = True
    while running:
        # Close event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # UPDATE HERE

        # Fill the background
        screen.fill(colors.BLACK.rgb)

        # DRAW HERE

        scaleddisplay.flip()

        # Timing loop
        clock.tick_busy_loop(framerate)


if __name__ == "__main__":
    main()
