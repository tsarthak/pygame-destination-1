from football.ShapeDescriptor import ShapeDescriptor


# Represents a game item. Every object drawn in the game is a Item for the most part.
class Item:
    def __init__(self, shape_desc: ShapeDescriptor) -> None:
        self._shape_descriptor = shape_desc
        pass

    def draw(self, surface, *args, **kwargs):
        self._shape_descriptor.make_shape(surface, *args, **kwargs)
