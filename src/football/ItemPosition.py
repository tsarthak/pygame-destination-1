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
