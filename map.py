import random
class Overworld:
    ORIGIN = [0, 0]

    enemies = []
    items = []

    def generateDestination():
        destination = []
        
        #determine north-south trajectory
        #if 0, north; if 1, south
        yAxis = random.randrange(0, 1)

        #determine west-east trajectory
        #if 0, west; if 1, east
        xAxis = random.randrange(0, 1)

        if xAxis is 0:
            destination.extend(random.randrange(-30, -15))
        else:
            destination.extend(random.randrange(15, 30))

        if yAxis is 0:
            destination.extend(random.randrange(15, 30))
        else:
            destination.extend(random.randrange(-30, -15))

        return destination

    DESTINATION = generateDestination()

class WorldChunk:
    """Making chunks 3 x 3 for now"""
    SIZE = 3

    xPos = 0
    yPos = 0

    def populateNodes():
        #Using generic random generation 0-4
        #for each direction or no direction
        area = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                row.extend(random.randrange(0, 4))
                           
            area.append(row)

    AREA = populateNodes()
        

class WorldNode:
    enemies = []
    items = []
    exitDirections = []

    xPos = 0
    yPos = 0

    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

    def addItem(item):
        items.extend(item)

    def addEnemy(enemy):
        enemies.extend(enemy)

    def removeEnemy(enemy):
        enemies.remove(enemy)

    def removeItem(item):
        items.remove(item)

    def addDirection(direction):
        direction.lower()
        self.directions.extend(direction)
        
    def hasNorthExit():
        return "north" in exitDirections
    def hasSouthExit():
        return "south" in exitDirections
    def hasEastExit():
        return "east" in exitDirections
    def hasWestExit():
        return "west" in exitDirections
