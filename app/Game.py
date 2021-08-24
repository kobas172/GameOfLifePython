import pygame
from app.Menu import *
import sys
from app.World import *


class Game:

    def __init__(self):
        pygame.init()
        self.run = True
        self.simulation = False
        self.windowWidth, self.windowHeight = 800, 600
        self.display = pygame.Surface((self.windowWidth, self.windowHeight))
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        self.fontName = 'app\\utilities\\Plaguard-ZVnjx.otf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.UP_KEY, self.DOWN_KEY = False, False
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.ENTER_KEY = False
        self.ESCAPE_KEY = False
        self.background = pygame.image.load("app\\utilities\\wallpaper.bmp")
        pygame.display.set_caption("World Simulation")
        self.menu = MainMenu(self)
        self.newSize = None
        self.world = None
        # self.world.loadFromFile()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESCAPE_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

    def gameLoop(self):
        while self.simulation:
            self.checkEvents()
            self.display.fill(self.BLACK)
            self.display.blit(self.background, (0, 0))
            self.draw("World Simulation", 40, 200, self.windowHeight / 8)
            self.window.blit(self.display, (0, 0))
            self.simulateGame()
            pygame.display.update()
            self.resetKeys()

    def draw(self, text, size, x, y):
        font = pygame.font.Font(self.fontName, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def resetKeys(self):
        self.DOWN_KEY, self.UP_KEY = False, False
        self.ENTER_KEY = False
        self.ESCAPE_KEY = False
        self.RIGHT_KEY, self.LEFT_KEY = False, False

    def credits(self):
        while True:
            self.checkEvents()
            self.display.fill(self.BLACK)
            self.display.blit(self.background, (0, 0))
            self.draw("World Simulation", 40, self.windowWidth / 3, self.windowHeight / 6)
            self.draw("PYTHON PYGAME", 40, self.windowWidth / 3, self.windowHeight / 6 + 50)
            self.draw("Piotr Gorkowski", 40, self.windowWidth / 3, self.windowHeight / 6 + 100)
            self.draw("184515", 40, self.windowWidth / 3, self.windowHeight / 6 + 150)
            self.draw("Press ESC to return", 20, 150, self.windowHeight - 100)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            if self.ESCAPE_KEY:
                self.resetKeys()
                break

    def initializeGame(self):
        isSetWidth = False
        isSetHeight = False
        width = 5
        height = 5
        self.resetKeys()
        while True:
            self.checkEvents()
            self.display.fill(self.BLACK)
            self.display.blit(self.background, (0, 0))
            self.draw("World Simulation", 40, self.windowWidth / 3, self.windowHeight / 6)
            self.draw("Set world size: ", 40, self.windowWidth / 3, self.windowHeight / 6 + 50)
            self.draw("Set width: " + str(width), 40, self.windowWidth / 3, self.windowHeight / 6 + 100)
            self.draw("Set height: " + str(height), 40, self.windowWidth / 3, self.windowHeight / 6 + 150)
            self.draw("Apply!", 40, self.windowWidth / 3, self.windowHeight / 6 + 200)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            if not isSetWidth:
                if self.LEFT_KEY and width > 5:
                    width -= 1
                if self.RIGHT_KEY and width < 23:
                    width += 1
                if self.ENTER_KEY:
                    isSetWidth = True
                self.resetKeys()
            if not isSetHeight and isSetWidth:
                if self.LEFT_KEY and height > 5:
                    height -= 1
                if self.RIGHT_KEY and height < 18:
                    height += 1
                if self.ENTER_KEY:
                    isSetHeight = True
                self.resetKeys()
            if self.ENTER_KEY:
                temp = Coordinates(width, height)
                self.newSize = temp
                self.world = World(self.newSize)
                self.world.initWorld()
                self.resetKeys()
                break

    def load(self):
        y = 0
        x = 0
        round = 0
        FILE = open("world.txt", "r")
        arr = [x.replace("\n", "").split() for x in FILE.readlines()]
        result = [list(x) for x in arr]
        for i, line in enumerate(result):
            if not i:
                y = int(line[0])
                x = int(line[1])
                round = int(line[2])
        FILE.close()
        self.newSize = Coordinates(y, x)
        self.world = World(self.newSize)
        self.world.setRound(round)
        self.world.loadFromFile()

    def simulateGame(self):
        self.printWorld()
        self.world.increment()

        for organism in self.world.getOrganismVector():
            organism.setAge(organism.getAge() + 1)
            if isinstance(organism, Human):
                self.printWorld()
                self.draw("Your turn!", 15, 600, 15)
                if self.world.getToNext() >= 4 and not self.world.getSuperPower():
                    self.draw("Immortality : " + str(self.world.getSuperPower()), 15, 600, 30)
                    self.draw("Do you want to turn on immortality? y or n", 15, 600, 45)
                    self.draw("Move with your arrow keys: ", 15, 600, 60)
                else:
                    self.draw("Immortality : " + str(self.world.getSuperPower()), 15, 600, 30)
                    self.draw("Move with your arrow keys: ", 15, 600, 45)
                self.window.blit(self.display, (0, 0))
                pygame.display.update()

            if organism.getAge() > 1:
                organism.action()

        self.draw("Round number: " + str(self.world.getRound()), 15, 600, 90)
        for i, com in enumerate(self.world.getList()):
            if i < 32:
                self.draw(com, 15, 600, 15*(i+9))
                self.window.blit(self.display, (0, 0))
                pygame.display.update()
        self.world.resetCom()
        self.printWorld()

        temp = False
        while not temp:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    temp = True
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        self.display.fill(self.BLACK)
        self.display.blit(self.background, (0, 0))
        self.draw("World Simulation", 40, 200, self.windowHeight / 8)
        self.window.blit(self.display, (0, 0))
        self.printWorld()

        self.draw("Do you want to save? y or n ", 15, 600, 75)
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

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
            self.world.saveToFile()
            pygame.quit()
            sys.exit()

    def printWorld(self):
        worldSize = self.world.getSize()
        x = 20
        y = self.windowHeight / 6
        w = 20
        for row in range(worldSize.y):
            for col in range(worldSize.x):
                if not self.world.getWorldMap()[row][col]:
                    box = pygame.Rect(x, y, w, w)
                    pygame.draw.rect(self.display, self.WHITE, box)
                    self.window.blit(self.display, (0, 0))
                else:
                    image = pygame.image.load(self.world.getWorldMap()[row][col].getImage())
                    self.display.blit(image, (x, y))
                    self.window.blit(self.display, (0, 0))
                x = x + w + 1
            y = y + w + 1
            x = 20
        pygame.display.update()
