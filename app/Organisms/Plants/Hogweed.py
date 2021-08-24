from app.Organisms.Plant import Plant
from app.Coordinates import Coordinates
from app.Organisms.Animal import Animal


class Hogweed (Plant):

    def __init__(self, world, location):
        super().__init__(world, 10, 0, "H", "app\\utilities\\hogweed.bmp", location)

    def reproduce(self, dest):
        self._world.appendToList("Hogweed reproduces!")
        Hogweed(self._world, dest)

    def action(self):
        self.checker()
        super().action()

    def checker(self):
        toCheck = Coordinates(self.getLoc().y, self.getLoc().x)
        toCheck.x = toCheck.x + 1
        self.killAnimal(toCheck)
        toCheck.x = toCheck.x - 2
        self.killAnimal(toCheck)
        toCheck.x = toCheck.x + 1
        toCheck.y = toCheck.y - 1
        self.killAnimal(toCheck)
        toCheck.y = toCheck.y + 2
        self.killAnimal(toCheck)

    def isAnimal(self, coords):
        if isinstance(self._world.getWorldMap()[coords.y][coords.x], Animal):
            return True
        return False

    def killAnimal(self, coords):
        if not self._world.isOutside(coords) and self._world.getWorldMap()[coords.y][coords.x] != None:
            if self.isAnimal(coords) and self._world.getWorldMap()[coords.y][coords.x].getName() != 'C':
                if self._world.getWorldMap()[coords.y][coords.x].getName() == '#' and not self._world.getSuperPower():
                    self._world.appendToList("Hogweed kills " + self._world.getWorldMap()[coords.y][coords.x].getName())
                    self._world.deleteOrganism(self._world.getWorldMap()[coords.y][coords.x])

