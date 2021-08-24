import pygame


class Menu:

    def __init__(self, game):
        self.game = game
        self.leftWidth, self.leftHeight = self.game.windowWidth / 4, self.game.windowHeight / 4
        self.runMenu = True
        self.cursor_rect = pygame.Rect(0, 0, 30, 30)
        self.offset = 200
        self.cursorImage = pygame.image.load("app\\utilities\\dot.bmp")

    def drawcursor_rect(self):
        self.game.display.blit(self.cursorImage, (self.cursor_rect.x-25, self.cursor_rect.y-18))

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.resetKeys()


class MainMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.StartX, self.StartY = self.leftWidth, self.leftHeight + 50
        self.LoadX, self.LoadY = self.leftWidth, self.leftHeight + 100
        self.creditsX, self.creditsY = self.leftWidth, self.leftHeight + 150
        self.cursor_rect.midtop = (self.StartX + self.offset, self.StartY)
        self.background = pygame.image.load("app\\utilities\\wallpaper.bmp")

    def displayMenu(self):
        self.runMenu = True
        while self.runMenu:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.display.blit(self.background, (0, 0))
            self.game.draw('Main Menu', 60, self.game.windowWidth / 4, self.game.windowHeight / 4 - 50)
            self.game.draw("Start Game", 50, self.StartX, self.StartY)
            self.game.draw("Load", 50, self.LoadX, self.LoadY)
            self.game.draw("Credits", 50, self.creditsX, self.creditsY)
            self.drawcursor_rect()
            self.blitScreen()

    def movecursor_rect(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.LoadX + self.offset, self.LoadY)
                self.state = 'Load'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.StartX + self.offset, self.StartY)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsX + self.offset, self.creditsY)
                self.state = 'Credits'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.StartX + self.offset, self.StartY)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.LoadX + self.offset, self.LoadY)
                self.state = 'Load'

    def checkInput(self):
        self.movecursor_rect()
        if self.game.ENTER_KEY:
            if self.state == 'Start':
                self.game.initializeGame()
                self.game.simulation = True
                self.runMenu = False
            elif self.state == 'Load':
                self.game.load()
                self.game.simulation = True
                self.runMenu = False
            elif self.state == 'Credits':
                self.game.credits()

