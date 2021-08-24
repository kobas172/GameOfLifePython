from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates
from random import randint


class Antelope (Animal):

    def __init__(self, world, location):
        super().__init__(world, 4, 4, "A", "app\\utilities\\antelope.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("Antelope reproduces")
            Antelope(self._world, freePlace)
        else:
            self._world.appendToList("Antelope: There is no place to reproduce!")

    def makeMove(self, counter):
        counter = counter + 1
        move = randint(0, 3)
        temp = Coordinates(0, 0)
        loc = self.getLoc()
        field = self._world.findField(loc.y, loc.x)
        if move == 0 and counter <= 98:
            temp.y = 2
        elif move == 1 and counter <= 98:
            temp.y = -2
        elif move == 2 and counter <= 98:
            temp.x = 2
        elif move == 3 and counter <= 98:
            temp.x = -2
        elif counter > 98 and not self._world.isOutside(field):
            self._world.appendToList(self._name + " moved to ( " + field.x + " " + field.y + " )")
            self.move(field)
        self.makeMoveToField(temp, counter)

    def fight(self, attacker, defender):
        possibility = randint(0, 1)
        coords = defender.getLoc()
        coordinates = self._world.findField(defender.getLoc().y, defender.getLoc().x)
        if not possibility and not self._world.isOutside(coordinates):
            self._world.appendToList("Antelope fled away!")
            self.move(coordinates)
            self._world.moveOrganism(attacker, coords)
        else:
            super().fight(attacker, defender)
