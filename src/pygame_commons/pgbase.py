import os
import pygame as pg
import logging


# set colors for quick reference
# colors in pygame are RGB tuples
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}


def set_logo():
    # Set a logo
    game_logo_path = os.path.join(os.path.dirname(
        __file__), "..", "..", "resources/my_game_icon.jpeg")
    logging.debug("Icon resource path - {game_logo_path}")
    game_logo = pg.image.load(game_logo_path)
    pg.display.set_icon(game_logo)
    logging.debug("Set game window logo..")


def set_game_window_title(title):
    # Set a window title
    pg.display.set_caption(title)


def set_background(surface, bkg_color):
    surface.fill(bkg_color)


def setup_display_surface(screen_height, screen_width, bkg_color=colors["white"]):
    display_surface = pg.display.set_mode((screen_width, screen_height))
    set_background(display_surface, bkg_color)
    return display_surface
