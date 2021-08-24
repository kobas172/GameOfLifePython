from app.Coordinates import Coordinates
from abc import ABC, abstractmethod
from random import randint


class Organism(ABC):

    def __init__(self, world, strength: int, initiative: int, name: str, image: str, location: Coordinates):
        self._world = world
        self._age = 0
        self._strength = strength
        self._initiative = initiative
        self._name = name
        self._image = image
        self._location = location
        world.addToMap(self)
        world.addToVector(self)

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, org):
        pass

    def getImage(self):
        return self._image

    def getLoc(self):
        return self._location

    def getName(self):
        return self._name

    def getStrength(self):
        return self._strength

    def getAge(self):
        return self._age

    def getInitiative(self):
        return self._initiative

    def setAge(self, age):
        self._age = age

    def setLoc(self, location):
        self._location = location

    def setStrength(self, strength):
        self._strength = strength

    def move(self, dest):
        self._world.getWorldMap()[dest.y][dest.x] = self._world.getWorldMap()[self._location.y][self._location.x]
        self._world.getWorldMap()[self._location.y][self._location.x] = None
        self.setLoc(dest)

