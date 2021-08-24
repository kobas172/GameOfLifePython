from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates


class Wolf (Animal):

    def __init__(self, world, location):
        super().__init__(world, 9, 5, "W", "app\\utilities\\wolf.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("Wolf reproduces")
            Wolf(self._world, freePlace)
        else:
            self._world.appendToList("Wolf: There is no place to reproduce!")
