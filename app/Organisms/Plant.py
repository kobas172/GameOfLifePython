from abc import abstractmethod
from app.Organism import Organism
from app.Coordinates import Coordinates
from random import randint


class Plant(Organism):

    def __init__(self, world, strength: int, initiative: int, name: str, image: str, location: Coordinates):
        super().__init__(world, strength, initiative, name, image, location)

    @abstractmethod
    def reproduce(self, dest):
        pass

    def action(self):
        probability = randint(0, 100)
        if probability > 90:
            freePlace = self._world.findField(self.getLoc().y, self.getLoc().x)
            if not self._world.isOutside(freePlace):
                self.reproduce(freePlace)
            #else:
                #self._world.appendToList("There is no place to reproduce!")

    def collision(self, org):
        self.fight(org, self)

    def fight(self, attacker, defender):
        if attacker.getName() == '#' and self._world.getSuperPower() and attacker.getStrength() < defender.getStrength():
            self._world.appendToList("You escaped to safe square!")
            newCoo = self._world.findField(self.getLoc().y, self.getLoc().x)
            if not self._world.isOutside(newCoo):
                self._world.moveOrganism(attacker, newCoo)
        else:
            call = "Fight between " + attacker.getName() + " and " + defender.getName()
            if attacker.getStrength() >= defender.getStrength():
                newLoc = defender.getLoc()
                call = call + " won " + attacker.getName()
                self._world.moveOrganism(attacker, newLoc)
                self._world.deleteFromVector(defender)
            else:
                call = call + " won " + defender.getName()
                self._world.deleteOrganism(attacker)
            self._world.appendToList(call)
