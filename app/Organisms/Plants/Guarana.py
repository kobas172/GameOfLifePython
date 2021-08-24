from app.Organisms.Plant import Plant
from app.Coordinates import Coordinates


class Guarana (Plant):

    def __init__(self, world, location):
        super().__init__(world, 0, 0, "U", "app\\utilities\\guarana.bmp", location)

    def reproduce(self, dest):
        self._world.appendToList("Guarana reproduces!")
        Guarana(self._world, dest)

    def fight(self, attacker, defender):
        attacker.setStrength(attacker.getStrength()+3)
        super().fight(attacker, defender)

