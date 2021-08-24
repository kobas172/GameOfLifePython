from random import shuffle
from app.Coordinates import Coordinates
from app.Organisms.Animals.Wolf import Wolf
from app.Organisms.Animals.Sheep import Sheep
from app.Organisms.Animals.Tortoise import Tortoise
from app.Organisms.Animals.Fox import Fox
from app.Organisms.Animals.Antelope import Antelope
from app.Organisms.Animals.SuperSheep import SuperSheep
from app.Organisms.Animals.Human import Human
from app.Organisms.Plants.Grass import Grass
from app.Organisms.Plants.Dandelion import Dandelion
from app.Organisms.Plants.Guarana import Guarana
from app.Organisms.Plants.WolfBerries import WolfBerries
from app.Organisms.Plants.Hogweed import Hogweed


class World:

    def __init__(self, size):
        self._size = size
        self._round = 0
        self._isGameOn = True
        self._worldMap = [[None for x in range(size.x)] for _ in range(size.y)]
        self._organismVector = list()
        self._superPower = False
        self._rounds = 0
        self._toNext = 5
        self._communicationArray = list()

    def getRand(self, arr):
        i = Coordinates(randint(0, self._size.y - 1), randint(0, self._size.x - 1))
        while i in arr:
            i = Coordinates(randint(0, self._size.y - 1), randint(0, self._size.x - 1))
        return i

    def initWorld(self):
        arr = [Coordinates(y, x) for x in range(self._size.x) for y in range(self._size.y)]
        shuffle(arr)
        Wolf(self, arr[0]).setAge(1)
        Wolf(self, arr[1]).setAge(1)
        Sheep(self, arr[2]).setAge(1)
        Sheep(self, arr[3]).setAge(1)
        Fox(self, arr[4]).setAge(1)
        Fox(self, arr[5]).setAge(1)
        Antelope(self, arr[6]).setAge(1)
        Antelope(self, arr[7]).setAge(1)
        Tortoise(self, arr[8]).setAge(1)
        Tortoise(self, arr[9]).setAge(1)
        SuperSheep(self, arr[10]).setAge(1)
        SuperSheep(self, arr[11]).setAge(1)
        Human(self, arr[12]).setAge(1)
        Grass(self, arr[13]).setAge(1)
        Dandelion(self, arr[14]).setAge(1)
        Guarana(self, arr[15]).setAge(1)
        Hogweed(self, arr[16]).setAge(1)
        WolfBerries(self, arr[17]).setAge(1)

    def setLoadedWorld(self, y, x):
        temp = Coordinates(y, x)
        self._size = temp
        self._worldMap = [[None for x in range(self._size.x)] for _ in range(self._size.y)]

    def increment(self):
        self._round += 1

    def getRound(self):
        return self._round

    def appendToList(self, text):
        self._communicationArray.append(text)

    def getList(self):
        return self._communicationArray

    def drawWorld(self):
        for row in range(self._size.y):
            for col in range(self._size.x):
                if not self._worldMap[row][col]:
                    print(".", end="")
                else:
                    print(self._worldMap[row][col].getName(), end="")
            print("")

    def makeMove(self):
        for organism in self._organismVector:
            organism.setAge(organism.getAge() + 1)
            if organism.getAge() > 1:
                organism.action()
        self.printList()
        self._communicationArray = list()

    def getVector(self):
        return self._organismVector

    def resetCom(self):
        self._communicationArray = list()

    def addToMap(self, organism):
        self._worldMap[organism.getLoc().y][organism.getLoc().x] = organism

    def addToVector(self, organism):
        self._organismVector.append(organism)
        self._organismVector.sort(key=lambda x: (x._initiative, x._age), reverse=True)

    def getWorldMap(self):
        return self._worldMap

    def setWorldMap(self, organism, y, x, value, y1, x1):
        self._worldMap[y][x] = organism
        self._worldMap[y1][x1] = value

    def getOrganismVector(self):
        return self._organismVector

    def getSize(self):
        return self._size

    def getSuperPower(self):
        return self._superPower

    def getToNext(self):
        return self._toNext

    def getRounds(self):
        return self._rounds

    def setRound(self, round):
        self._round = round

    def setSuperPower(self, superPower):
        self._superPower = superPower

    def setToNext(self, toNext):
        self._toNext = toNext

    def setRounds(self, rounds):
        self._rounds = rounds

    def isOutside(self, dest):
        if dest.x >= self._size.x or dest.x < 0 or dest.y >= self._size.y or dest.y < 0:
            return True
        return False

    def detectedCollision(self, dest):
        return self._worldMap[dest.y][dest.x]

    def findField(self, y, x):
        temp = Coordinates(y, x)
        temp.x = temp.x + 1
        if not self.isOutside(temp) and not self._worldMap[temp.y][temp.x]:
            return temp
        temp.x = temp.x - 2
        if not self.isOutside(temp) and not self._worldMap[temp.y][temp.x]:
            return temp
        temp.x, temp.y = x, temp.y + 1
        if not self.isOutside(temp) and not self._worldMap[temp.y][temp.x]:
            return temp
        temp.y = temp.y - 2
        if not self.isOutside(temp) and not self._worldMap[temp.y][temp.x]:
            return temp
        temp.x, temp.y = -1, -1
        return temp

    def moveOrganism(self, organism, newLoc):
        self._worldMap[organism.getLoc().y][organism.getLoc().x], self._worldMap[newLoc.y][newLoc.x] = None, organism
        organism.setLoc(newLoc)

    def deleteOrganism(self, organism):
        for i, org in enumerate(self._organismVector):
            if org == organism:
                self._worldMap[organism.getLoc().y][organism.getLoc().x] = None
                break
        self._organismVector.remove(organism)

    def deleteFromVector(self, organism):
        self._organismVector.remove(organism)

    def chooseHogweed(self, superSheep):
        loc = Coordinates(superSheep.getLoc().y, superSheep.getLoc().x)
        sum = self._size.y + self._size.x
        chosenHogweed = None
        for organism in self._organismVector:
            if isinstance(organism, Hogweed) and abs(organism.getLoc().y - loc.y) + abs(organism.getLoc().x - loc.x) < sum:
                sum = abs(organism.getLoc().y - loc.y) + abs(organism.getLoc().x - loc.x)
                chosenHogweed = organism
        return chosenHogweed

    def saveToFile(self):
        FILE = open("world.txt", "w")
        FILE.write(str(self._size.y) + " " + str(self._size.x) + " " + str(self._round) + "\n")
        for organism in self._organismVector:
            if isinstance(organism, Human):
                FILE.write(organism.getName() + " " + str(organism.getLoc().y) + " " + str(organism.getLoc().x) + " " + str(organism.getStrength()) + " " + str(organism.getInitiative()) + " " + str(organism.getAge()) + " " + organism.getImage() + " " + str(self._superPower) + " " + str(self._rounds) + " " + str(self._toNext) + "\n")
            else:
                FILE.write(organism.getName() + " " + str(organism.getLoc().y) + " " + str(organism.getLoc().x) + " " + str(organism.getStrength()) + " " + str(organism.getInitiative()) + " " + str(organism.getAge()) + " " + organism.getImage() + "\n")
        FILE.close()

    def loadFromFile(self):
        FILE = open("world.txt", "r")
        arr = [x.replace("\n", "").split() for x in FILE.readlines()]
        result = [list(x) for x in arr]
        for i, line in enumerate(result):
            if i:
                if line[0] == "W":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Wolf(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "S":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Sheep(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "F":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Fox(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "T":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Tortoise(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "A":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Antelope(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "G":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Grass(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "D":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Dandelion(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "U":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Guarana(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "B":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = WolfBerries(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "H":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Hogweed(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "C":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = SuperSheep(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                elif line[0] == "#":
                    coords = Coordinates(int(line[1]), int(line[2]))
                    newOrg = Human(self, coords)
                    newOrg.setStrength(int(line[3]))
                    newOrg.setAge(int(line[5]))
                    self.setSuperPower(bool(line[7]))
                    self.setRounds(int(line[8]))
                    self.setToNext(int(line[9]))
        FILE.close()

