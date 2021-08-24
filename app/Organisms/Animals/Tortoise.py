from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates
from random import randint


class Tortoise (Animal):

    def __init__(self, world, location):
        super().__init__(world, 2, 1, "T", "app\\utilities\\tortoise.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("Tortoise reproduces")
            Tortoise(self._world, freePlace)
        else:
            self._world.appendToList("Tortoise: There is no place to reproduce!")

    def makeMove(self, counter):
        willMove = randint(0, 3)
        if not willMove:
            super().makeMove(counter)
        else:
            self._world.appendToList("Tortoise stays on his place!")

    def fight(self, attacker, defender):
        if attacker.getStrength() < 5 and defender.getName() == 'T':
            self._world.appendToList("Tortoise pushed back the attack!")
        else:
            super().fight(attacker, defender)
