import pygame

input_surface = None
output_surface = None


def set_mode(surface_size, window_size):
    """Initialize a window or screen for display

    This function will create a display Surface.

    The surface_size argument is a pair of numbers representing the width and height of the input surface.
    The window_size argument is a pair of numbers representing the width and height of the window output.

    The Surface that gets returned can be drawn to like a regular Surface but changes will eventually be seen on the monitor.
    Before the image is drawn to the screen, the input surface will be scaled up to fit window output.

    Parameters
    ----------
    surface_size
        The size of input surface that you will be able to write to.
    window_size
        The size of the window output the surface will be displayed on. The input surface will automatically scale to fit this.

    Returns
    -------
        The actual number of nanoseconds used.
    """
    global input_surface
    global output_surface

    input_surface = pygame.Surface(surface_size)
    output_surface = pygame.display.set_mode(window_size)

    return input_surface


def flip():
    """Update the full display Surface to the screen

    This will update the contents of the entire display.
    The input surface will automatically be scaled to fit the window output.
    """
    # Pixel-scale the input_surface onto the output_surface
    pygame.transform.scale(input_surface, output_surface.get_size(), output_surface)
    pygame.display.flip()
