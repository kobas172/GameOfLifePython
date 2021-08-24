from abc import abstractmethod
from app.Organism import Organism
from app.Coordinates import Coordinates
from random import randint


class Animal(Organism):

    def __init__(self, world, strength: int, initiative: int, name: str, image: str, location: Coordinates):
        super().__init__(world, strength, initiative, name, image, location)

    def action(self):
        self.makeMove(1)

    def makeMove(self, counter):
        counter = counter + 1
        move = randint(0, 3)
        temp = Coordinates(0, 0)
        loc = self.getLoc()
        field = self._world.findField(loc.y, loc.x)
        if move == 0 and counter <= 98:
            temp.y = 1
        elif move == 1 and counter <= 98:
            temp.y = -1
        elif move == 2 and counter <= 98:
            temp.x = 1
        elif move == 3 and counter <= 98:
            temp.x = -1
        elif counter > 98 and not self._world.isOutside(field):
            call = self._name + " moved to ( " + field.x + " " + field.y + " )"
            self._world.appendToList(call)
            self.move(field)
        self.makeMoveToField(temp, counter)

    def collision(self, org):
        if self.sameType(org):
            self.reproduce(org)
        else:
            self.fight(org, self)

    def sameType(self, org):
        if self.getName() == org.getName():
            return True
        return False

    def makeMoveToField(self, dest, counter):
        newLoc = Coordinates(self.getLoc().y+dest.y, self.getLoc().x+dest.x)
        org = None
        if not self._world.isOutside(newLoc):
            org = self._world.detectedCollision(newLoc)
        if self._world.isOutside(newLoc) and counter < 100:
            self.makeMove(counter)
        elif org:
            org.collision(self)
        else:
            if counter < 100:
                call = self._name + " moved to ( " + str(newLoc.x) + " " + str(newLoc.y) + " )"
                self._world.appendToList(call)
                self.move(newLoc)

    @abstractmethod
    def reproduce(self, org):
        pass

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
