import pygame
from app.Organisms.Animal import Animal
from app.Coordinates import Coordinates
import sys


class Human (Animal):

    def __init__(self, world, location):
        super().__init__(world, 5, 4, "#", "app\\utilities\\human.bmp", location)

    def reproduce(self, org):
        pass

    def action(self):
        self.immortality()
        self.makeMove(1)

    def immortality(self):
        if self._world.getSuperPower():
            self._world.setRounds(self._world.getRounds() + 1)
            if self._world.getRounds() == 5:
                self._world.setSuperPower(False)
                self._world.setToNext(0)
        else:
            self._world.setToNext(self._world.getToNext() + 1)
            if self._world.getToNext() >= 5:
                case = True
                super = False
                while case:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_y:
                                super = True
                                case = False
                            elif event.key == pygame.K_n:
                                case = False
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                if super:
                    self._world.setSuperPower(True)
                    self._world.setRounds(1)

    def makeMove(self, counter):
        counter += 1
        temp = Coordinates(0, 0)
        case = True
        while case:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        temp.y = -1
                        case = False
                    elif event.key == pygame.K_DOWN:
                        temp.y = 1
                        case = False
                    elif event.key == pygame.K_RIGHT:
                        temp.x = 1
                        case = False
                    elif event.key == pygame.K_LEFT:
                        temp.x = -1
                        case = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        self.makeMoveToField(temp, counter)

    def collision(self, org):
        if not self._world.getSuperPower() or self.getStrength() > org.getStrength():
            super().collision(org)
        else:
            newCoo = self._world.findField(self.getLoc().y, self.getLoc().x)
            if not self._world.isOutside(newCoo):
                self.move(newCoo)
