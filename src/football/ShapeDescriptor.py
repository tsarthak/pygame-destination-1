import math
from football.ShapeTypes import ShapeTypes
from football.ItemPosition import Position
import pygame_commons.pgbase as pgbase
import pygame.draw as pgdraw

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
