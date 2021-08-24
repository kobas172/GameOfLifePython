from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates


class SuperSheep (Animal):

    def __init__(self, world, location):
        super().__init__(world, 11, 4, "C", "app\\utilities\\supersheep.bmp", location)

    def reproduce(self, org):
        loc = self.getLoc()
        freePlace = self._world.findField(loc.y, loc.x)
        if not self._world.isOutside(freePlace):
            self._world.appendToList("SuperSheep reproduces")
            SuperSheep(self._world, freePlace)
        else:
            self._world.appendToList("SuperSheep: There is no place to reproduce!")

    def find(self):
        return self._world.chooseHogweed(self)

    def makeMove(self, counter):
        counter += 1
        obj = self.find()
        temp = Coordinates(0, 0)
        if obj:
            if obj.getLoc().y != self.getLoc().y:
                if obj.getLoc().y > self.getLoc().y:
                    temp.y = 1
                else:
                    temp.y = -1
            else:
                if obj.getLoc().x > self.getLoc().x:
                    temp.x = 1
                elif obj.getLoc().x < self.getLoc().x:
                    temp.x = -1
            super().makeMoveToField(temp, counter)
        else:
            super().makeMove(counter)

