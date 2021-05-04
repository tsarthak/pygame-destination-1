import pygame as pg
import os
import logging
import logging.handlers
import math

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

'''
Task 1 for student - using online RGB color pallette available at https://www.rapidtables.com/web/color/RGB_Color.html find out RGB codes for the following colors and fill them out in the above dictionary

1. Yellow
2. Cyan
3. Purple
4. Grey
5. Dark orchid
'''

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


def draw_circle(surface):
    pg.draw.circle(surface, color=colors['red'], center=[
        200, 350], radius=50, width=2)
    # student task 6 : draw a solid circle of radius 100


def main():
    # init the python game module.
    num_of_ok_init, num_of_bad_init = pg.init()
    logging.debug(
        "Number of successful inits {num_of_ok_init}. Number of bad inits {num_of_bad_init}")

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

    # # sample : draw lines
    # draw_sample_lines(display_surface)

    # # sample : draw rectangle
    # draw_rectangle(display_surface)

    # # sample : draw triangle
    # draw_triangle(display_surface)

    # # sample : draw a polygon
    # draw_polygon(display_surface)

    # # sample : draw circle
    # draw_circle(display_surface)
    x_start = 200
    y_start = 200
    r_72 = math.radians(72)
    r_54 = math.radians(54)

    side = 50
    points = [
        (x_start, y_start)
    ]
    points.append((points[0][0] + side, y_start))
    points.append((points[1][0] + side * math.cos(r_72),
                  points[1][1] - side * math.sin(r_72)))
    points.append((points[2][0] - side * math.sin(r_54),
                  points[2][1] - side * math.cos(r_54)))
    points.append((points[3][0] - side * math.sin(r_54),
                  points[3][1] + side * math.cos(r_54)))
    print(points)

    pg.draw.polygon(display_surface, colors['black'], points)

    game_running = True
    while game_running:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

    return


if __name__ == "__main__":
    main()
