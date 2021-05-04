import os
import math
import logging
import logging.handlers
import threading as th
from enum import Enum
import pygame as pg
import pygame.draw as pgdraw
from pygame import display
import pygame_commons.pgbase as pgbase

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)-10s] %(message)s", level=logging.INFO)


# enumerates the types of shapes
class ShapeTypes(Enum):
    SQUARE = 1
    CIRCLE = 2
    TRIANGLE = 3
    RECTANGLE = 4
    PENTAGON = 5


# Wraps the x,y coordinate as a Position object
class Position:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self) -> str:
        str = f"Position:(x={self._x},y={self._y})"
        return str

    def x(self):
        return self._x

    def y(self):
        return self._y


# Represents and responsible for drawing a shape on the game screen.
class ShapeDescriptor:
    def __init__(self, shape_typ: ShapeTypes, *args, **kwargs):
        self._shape_type = shape_typ
        self._shape_properties = kwargs
        return

    def __make_circle__(self, surface, *args, **kwargs):
        radius, center, color, width = None, None, pgbase.colors['black'], 0
        radius = kwargs['radius'] if 'radius' in kwargs else self._shape_properties['radius']
        center = kwargs['center'] if 'center' in kwargs else self._shape_properties['center']
        if 'color' in kwargs:
            color = pgbase.colors[kwargs['color']]
        elif 'color' in self._shape_properties:
            color = pgbase.colors[self._shape_properties['color']]
        if 'width' in kwargs:
            width = kwargs['width']
        elif 'width' in self._shape_properties:
            width = self._shape_properties['width']

        pgdraw.circle(
            surface,
            color,
            [center.x(), center.y()],
            radius,
            width
        )

    def __make_rectangle__(self, surface, *args, **kwargs):
        start, length, breadth, color, width = None, None, None, pgbase.colors['black'], 0
        start = kwargs['start'] if 'start' in kwargs else self._shape_properties['start']
        if 'side' in kwargs:
            length = breadth = kwargs['side']
        elif 'side' in self._shape_properties:
            length = breadth = self._shape_properties['side']
        elif 'length' in kwargs and 'breadth' in kwargs:
            breadth = kwargs['breadth']
            length = kwargs['length']
        elif 'length' in self._shape_properties and 'breadth' in self._shape_properties:
            breadth = self._shape_properties['breadth']
            length = self._shape_properties['length']
        else:
            raise Exception(
                "Insufficient arguments to make rectangle/square - one or all of side/length/breadth missing"
            )
        if 'color' in kwargs:
            color = pgbase.colors[kwargs['color']]
        elif 'color' in self._shape_properties:
            color = pgbase.colors[self._shape_properties['color']]
        if 'width' in kwargs:
            width = kwargs['width']
        elif 'width' in self._shape_properties:
            width = self._shape_properties['width']

        pgdraw.rect(
            surface,
            color,
            [start.x(), start.y(), length, breadth],
            width
        )

    def __make_triangle__(self, surface, *args, **kwargs):
        point_1, point_2, point_3, color, width = None, None, None, pgbase.colors['black'], 0
        point_1 = kwargs['point_1'] if 'point_1' in kwargs else self._shape_properties['point_1']
        point_2 = kwargs['point_2'] if 'point_2' in kwargs else self._shape_properties['point_2']
        point_3 = kwargs['point_3'] if 'point_3' in kwargs else self._shape_properties['point_3']
        if 'color' in kwargs:
            color = pgbase.colors[kwargs['color']]
        elif 'color' in self._shape_properties:
            color = pgbase.colors[self._shape_properties['color']]
        if 'width' in kwargs:
            width = kwargs['width']
        elif 'width' in self._shape_properties:
            width = self._shape_properties['width']

        pgdraw.polygon(
            surface,
            color,
            [
                (point_1.x(), point_1.y()),
                (point_2.x(), point_2.y()),
                (point_3.x(), point_3.y())
            ],
            width
        )

    def __make_pentagon__(self, surface, *args, **kwargs):
        color, width = pgbase.colors['black'], 0
        side = kwargs['side'] if 'side' in kwargs else self._shape_properties['side']
        center = kwargs['center'] if 'center' in kwargs else (
            self._shape_properties['center'] if 'center' in self._shape_properties else None
        )
        if center is None:
            start = kwargs['start'] if 'start' in kwargs else self._shape_properties['start']
        else:
            start = Position(center.x() - 0.5 * side, center.y() +
                             (0.5 * side * math.tan(math.radians(54))))
        if 'color' in kwargs:
            color = pgbase.colors[kwargs['color']]
        elif 'color' in self._shape_properties:
            color = pgbase.colors[self._shape_properties['color']]
        if 'width' in kwargs:
            width = kwargs['width']
        elif 'width' in self._shape_properties:
            width = self._shape_properties['width']
        # this will draw an upright pentagon
        r_72 = math.radians(72)
        r_54 = math.radians(54)
        points = [(start.x(), start.y())]
        points.append((points[0][0] + side, start.y()))
        points.append((points[1][0] + side * math.cos(r_72),
                       points[1][1] - side * math.sin(r_72)))
        points.append((points[2][0] - side * math.sin(r_54),
                       points[2][1] - side * math.cos(r_54)))
        points.append((points[3][0] - side * math.sin(r_54),
                       points[3][1] + side * math.cos(r_54)))
        pgdraw.polygon(
            surface,
            color,
            points,
            width
        )

    def make_shape(self, surface, *args, **kwargs):
        if self._shape_type == ShapeTypes.CIRCLE:
            self.__make_circle__(surface, *args, **kwargs)
        elif self._shape_type == ShapeTypes.RECTANGLE or self._shape_type == ShapeTypes.SQUARE:
            self.__make_rectangle__(surface, *args, **kwargs)
        elif self._shape_type == ShapeTypes.TRIANGLE:
            self.__make_triangle__(surface, *args, **kwargs)
        elif self._shape_type == ShapeTypes.PENTAGON:
            self.__make_pentagon__(surface, *args, **kwargs)
        return


# Represents a game item. Every object drawn in the game is a Item for the most part.
class Item:
    def __init__(self, shape_desc: ShapeDescriptor) -> None:
        self._shape_descriptor = shape_desc
        pass

    def draw(self, surface, *args, **kwargs):
        self._shape_descriptor.make_shape(surface, *args, **kwargs)


# represents a single character/ player. It derives from Item because it is an active game item
class Character(Item):
    def __init__(self, shape_desc: ShapeDescriptor, speed: int) -> None:
        super().__init__(shape_desc)
        self._movement_speed = speed
        return


# represents multiple characters in a team instance.
class Team:
    def __init__(self, team_size, formation: str, color):
        self._players = []
        temp = formation.split('-')
        self._formation = {
            "F": temp[0],
            "M": temp[1],
            "D": temp[2],
            "G": 1
        }
        self.__make_team__(team_size, color)

    def __make_team__(self, team_size, team_color):
        for count in range(0, team_size, 1):
            self._players.append(Character(
                ShapeDescriptor(
                    ShapeTypes.CIRCLE,
                    radius=10,
                    color=team_color
                ),
                3
            )
            )

    def __iter__(self):
        return iter(self._players)


def main():
    pg.init()
    if not pg.get_init():
        return

    pgbase.set_logo()
    pgbase.set_game_window_title("Futbol")
    surface = pgbase.setup_display_surface(500, 1000)

    players_in_team = 7
    # F-M-D
    formation = ["3-2-1", "1-3-2", "2-2-2"]

    team_1 = Team(5, formation[0], 'red')
    team_2 = Team(5, formation[2], 'blue')

    team1_y = 100
    for player in team_1:
        player.draw(surface, center=Position(100, team1_y))
        team1_y += 50

    team2_y = 100
    for player in team_2:
        player.draw(surface, center=Position(800, team2_y))
        team2_y += 50

    game_running = True
    while game_running:
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_running = False

    return


if __name__ == "__main__":
    main()
