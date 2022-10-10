import pyray
from game.shared.point import Point


class KeyboardService:
    #player input
    def __init__(self, cellSize = 1):
        #using cell size
        self._cell_size = cellSize

    def get_direction(self):
        #using piray methods to define the movement direction
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        #if pyray.is_key_down(pyray.KEY_UP):
        #    dy = -1
        
        #if pyray.is_key_down(pyray.KEY_DOWN):
        #    dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction