from app.Organisms.Plant import Plant
from app.Coordinates import Coordinates


class Grass (Plant):

    def __init__(self, world, location):
        super().__init__(world, 0, 0, "G", "app\\utilities\\grass.bmp", location)

    def reproduce(self, dest):
        self._world.appendToList("Grass reproduces!")
        Grass(self._world, dest)

