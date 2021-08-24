from app.Organisms.Plant import Plant
from app.Coordinates import Coordinates


class WolfBerries (Plant):

    def __init__(self, world, location):
        super().__init__(world, 99, 0, "B", "app\\utilities\\wolfberries.bmp", location)

    def reproduce(self, dest):
        self._world.appendToList("Wolf berries reproduces!")
        WolfBerries(self._world, dest)

    def fight(self, attacker, defender):
        if attacker.getName() == '#' and self._world.getSuperPower() and attacker.getStrength() < defender.getStrength():
            self._world.appendToList("You escaped to safe square!")
            newCoo = self._world.findField(self.getLoc().y, self.getLoc().x)
            if not self._world.isOutside(newCoo):
                self._world.moveOrganism(attacker, newCoo)
        else:
            self._world.appendToList("Fight between " + attacker.getName() + " and " + defender.getName() + " won " + defender.getName())
            self._world.deleteOrganism(attacker)
            self._world.deleteOrganism(defender)
