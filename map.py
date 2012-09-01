import random
class Overworld:
    ORIGIN = [0, 0]
    DESTINATION = generateDestination()

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

        if xAxis == 0:
            destination.extend(random.randrange(-30, -15))
        else:
            destination.extend(random.randrange(15, 30))

        if yAxis == 0:
            destination.extend(random.randrange(15, 30))
        else:
            destination.extend(random.randrange(-30, -15))

        return destination

class WorldChunk:
    """Making chunks 3 x 3 for now"""
    SIZE = 3
    AREA = populateNodes()

    def populateNodes():
        #Using generic random generation 0-4
        #for each direction or no direction
        area = []
        for i in range(SIZE):
            row = []
            for j in range(SIZE):
                row.extend(random.randrange(0, 4))
                           
            area.append(row)

        

class WorldNode:
    enemies = []
    items = []
    directions = []

    directionalCount = 0

    #inits node with number of directions available to it for generation
    def __init__(iDirections):
        self.directionalCount = iDirections

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
        return "north" in directions
    def hasSouthExit():
        return "south" in directions
    def hasEastExit():
        return "east" in directions
    def hasWestExit():
        return "west" in directions
    def north():

    def south():

    def east():

    def west():
