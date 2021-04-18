import pygame as pg
import os
import logging
import logging.handlers
from pygame import display
import pygame.draw as pgdraw

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)-10s] %(message)s", level=logging.INFO)

# set colors for quick reference
# colors in pygame are RGB tuples
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'black': (0, 0, 0),
    'white': (255, 255, 255)
}

#### GAME HELPER FUNCTIONS ####


def set_logo():
    # Set a logo
    game_logo_path = os.path.join(os.path.dirname(
        __file__), "..", "resources/my_game_icon.jpeg")
    logging.debug("Icon resource path - {game_logo_path}")
    game_logo = pg.image.load(game_logo_path)
    pg.display.set_icon(game_logo)
    logging.debug("Set game window logo..")


def set_game_window_title(title):
    # Set a window title
    pg.display.set_caption(title)


def create_game_display_surface(height, width):
    return pg.display.set_mode((width, height))  # , flags=pg.SCALED)


def set_background(surface, bkg_color):
    surface.fill(bkg_color)
#### GAME HELPER FUNCTIONS ####


# draw single lines on the screen
def draw_sample_lines(surface_obj):
    # single lines
    pg.draw.line(surface_obj, color=colors['red'], start_pos=(
        0, 200), end_pos=(500, 200), width=2)
    pg.draw.line(surface_obj, color=colors['black'], start_pos=(
        0, 150), end_pos=(324, 90), width=2)

    # multiple lines. used to draw a polygon or an unbounded figure
    base_coordinate = 100
    pg.draw.lines(surface_obj, color=colors['green'], closed=True, points=[
        (base_coordinate, base_coordinate),
        (base_coordinate - 90, base_coordinate),
        (55, 25)
    ], width=1)

    # student task 2 - draw 1 line of length 100, color it blue, with a width of 5


def draw_rectangle(surface):
    # solid rectangle
    pg.draw.rect(surface, color=colors['black'], rect=(250, 20, 200, 200))

    # rectangle with just a border
    pg.draw.rect(surface, color=colors['red'],
                 rect=(400, 400, 50, 50), width=2)

    # student task 3: draw a rectangle at (50, 50) with width 100 and height 75


def draw_triangle(surface):
    pg.draw.polygon(surface, colors['black'],
                    ((0, 500), (120, 500), (67, 442)))

    # student task 4 : draw a equilateral triangle of side length 10


def draw_polygon(surface):
    pg.draw.polygon(surface, color=colors['blue'],
                    points=((250, 500), (300, 500), (300, 450), (275, 425), (250, 450)))
    # student task 5 : draw a polygon in the shape of a house


def draw_circle(surface, center_coordinates):
    return pg.draw.circle(surface, color=colors['red'], center=center_coordinates, radius=50, width=2)
    # student task 6 : draw a solid circle of radius 100


def move_circle(display_surface, target):
    set_background(display_surface, colors['white'])
    return draw_circle(display_surface, target)


def main():
    # init the python game module.
    num_of_ok_init, num_of_bad_init = pg.init()
    logging.debug(
        f"Number of successful inits {num_of_ok_init}. Number of bad inits {num_of_bad_init}")

    # check if the game is correctly init.
    if pg.get_init() == False:
        return
    logging.info("Game initialized. Starting..")

    # set game logo
    set_logo()

    # set game window title
    set_game_window_title("MyFirstPyGame")

    # set up the window of the game
    display_surface = create_game_display_surface(500, 500)

    # set the background
    set_background(display_surface, colors['white'])

    # sample : draw circle
    circle_coordinates = [200, 200]
    draw_circle(display_surface, circle_coordinates)

    game_running = True
    move_step = 5
    while game_running:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False
            elif event.type == pg.KEYDOWN:
                if pg.key.get_focused():  # get if we are receiving inputs from the keyboard
                    if pg.key.get_pressed()[pg.K_RIGHT] and circle_coordinates[0] < 450:
                        circle_coordinates[0] += move_step
                    elif pg.key.get_pressed()[pg.K_LEFT] and circle_coordinates[0] > 50:
                        circle_coordinates[0] -= move_step
                    elif pg.key.get_pressed()[pg.K_UP] and circle_coordinates[1] > 50:
                        circle_coordinates[1] -= move_step
                    elif pg.key.get_pressed()[pg.K_DOWN] and circle_coordinates[1] < 450:
                        circle_coordinates[1] += move_step
                    move_circle(display_surface, circle_coordinates)
    return


if __name__ == "__main__":
    main()
