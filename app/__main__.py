from app.Game import Game

g = Game()

while g.run:
    g.menu.displayMenu()
    g.simulation = True
    g.gameLoop()
