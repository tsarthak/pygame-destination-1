from football.ShapeDescriptor import ShapeDescriptor
from football.GameItem import Item


# represents a single character/ player. It derives from Item because it is an active game item
class Character(Item):
    def __init__(self, shape_desc: ShapeDescriptor, speed: int) -> None:
        super().__init__(shape_desc)
        self._movement_speed = speed
        return
