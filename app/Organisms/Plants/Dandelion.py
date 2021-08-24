from app.Organisms.Plant import Plant
from app.Coordinates import Coordinates


class Dandelion (Plant):

    def __init__(self, world, location):
        super().__init__(world, 0, 0, "D", "app\\utilities\\dandelion.bmp", location)

    def reproduce(self, dest):
        self._world.appendToList("Dandelion reproduces!")
        Dandelion(self._world, dest)

    def action(self):
        for i in range(3):
            super().action()

