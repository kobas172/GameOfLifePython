from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates


class Sheep (Animal):

    def __init__(self, world, location):
        super().__init__(world, 4, 4, "S", "app\\utilities\\sheep.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("Sheep reproduces")
            Sheep(self._world, freePlace)
        else:
            self._world.appendToList("Sheep: There is no place to reproduce!")
