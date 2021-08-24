from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates


class Fox (Animal):

    def __init__(self, world, location):
        super().__init__(world, 3, 7, "F", "app\\utilities\\fox.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("Fox reproduces")
            Fox(self._world, freePlace)
        else:
            self._world.appendToList("Fox: There is no place to reproduce!")

    def makeMoveToField(self, dest, counter):
        newLoc = Coordinates(self.getLoc().y+dest.y, self.getLoc().x+dest.x)
        org = None
        if not self._world.isOutside(newLoc):
            org = self._world.detectedCollision(newLoc)
        if (self._world.isOutside(newLoc) and counter < 100) or (isinstance(org, Animal) and counter < 100):
            self.makeMove(counter)
        elif org:
            org.collision(self)
        else:
            if counter < 100:
                call = self._name + " moved to ( " + str(newLoc.x) + " " + str(newLoc.y) + " )"
                self._world.appendToList(call)
                self.move(newLoc)
