from random import choice, choices, random, randrange
from copy import deepcopy

specialOptions = [
    "S",    # Start
    "E",    # End
    "K",    # key room
    "P"     # Puzzle room

]



options = [


    #"T",    # Trapped Room
    #" ",     # Nothing
    "R",    # Room
]

keyBlocks = [
      #please fill this with the names of blocks used
]

maxSections = 10        #maximum number of sections the dungeon can have
maxSectionSize = 10     #maximum number of rooms a section can have
maxChildren = 3        # Maximum number of children a section can have

inverseDir = {   # Just a dictionary for quickly getting an opposite direction
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e"
}

dirOffset = {   # A dictionary containing the offset corresponding to a direction
    "n": (0, 1),
    "e": (1, 0),
    "s": (0, -1),
    "w": (-1, 0)

}
# 3 x 3 (*2 for passageways -1 for edges)
length = 3 * 2 - 1
width = 3 * 2 - 1


class Room:         #Class for a single room
    def __init__(self, xy, depth, sectionID):
        self.xy = xy    # let's the room store it's own coordinates - this should be a tuple
        self.connections = {        #
            "n": False,     # Whether the room is connected to the north
            "e": False,     # Whether the room is connected to the east
            "s": False,     # Whether the room is connected to the south
            "w": False      # Whether the room is connected to the west
        }
        self.type = None    # the type of room the room is - should remain nothing until the entire dungeon is generated
        self.depth = depth  # how deep in the section the room is - useful for finding rooms at the end of a section
        self.connectionNum = 0
        self.sectionID = sectionID  #the ID of the section the room is in
        self.sectionEntrance = tuple((False, None))
        self.meta = False

    def getMeta(self, offset):
        if self.meta:
            return str(useOffset(self.xy, offset)) + ' ' + self.meta + '\n'
        return ''


    def getNeighbourPosition(self, direction):  #returns the grid position in the direction passed
        offset = dirOffset[direction]
        return tuple((self.xy[0] + offset[0], self.xy[1] + offset[1]))

    def recalculateConnectionCount(self):   #recaluclate the number of connections the room has
        self.connectionNum = 0
        for val in self.connections:
            if val is True:
                self.connectionNum += 1


class Section:      # Class for a section - a connected set of rooms
    def __init__(self, entrancePos, entranceDir, currentGrid, map, id, parent, onMainPath):      #passes the entrance position, entrance direction
                                                                    # a dictionary of positions already in use, the section's unique ID,
                                                                    #the section's parent, and if the section is on the main path
        self.map = map      #reference to the map
        self.id = id        #unique section id
        self.parent = parent    #reference to parent section
        self.onMainPath = onMainPath    #whether this section is on the main path
        self.children = []                  # A list of children sections.  Should only be added to after the section
                                            # has finished generating its rooms
        self.fullMap = currentGrid        # might not be needed, may remove later
        self.sectionMap = {entrancePos: Room(entrancePos, 0, id)}  # the map of rooms in this section
        self.sectionMap[entrancePos].sectionEntrance = tuple((True, entranceDir))     # mark the room as a section entrance
        self.entrance = tuple((entrancePos, entranceDir))
        if entranceDir is not None:     #only execute the next lines if this isn't the first section
            self.sectionMap[entrancePos].connections[entranceDir] = True    # set the initial room in the
                                                                            # section to be connected
            self.sectionMap[entrancePos].recalculateConnectionCount()
            self.sectionMap[entrancePos].type = '1'     # temporarily mark the entrance to this section
            parExit, parDir = self.getParentExit()
            self.map.map[parExit].type = '0'          # temporarily mark the room in the parent section leading to this section



    def getParentExit(self):
        parExit = self.sectionMap[self.entrance[0]].getNeighbourPosition(self.entrance[1])
        return parExit, inverseDir[self.entrance[1]]

    def roomCount(self):            # returns the number of rooms in the section
        return len(self.sectionMap)

    def newRoomChance(self):        # returns the probability another room will generate - modifiable if needed
                                    # current probability is 1 - (room count squared divided by max rooms squared)
        if self.roomCount() <= minSectionSize:
            return 1
        num = self.roomCount() - minSectionSize
        denom = maxSectionSize - minSectionSize
        if denom == 0:
            return -1

        return 1 - ((num * num) / (denom * denom))

    def newChildChance(self):       # returns the probability the section will attempt to generate an additional child
        chance = 1
        if self.children:       # if the section already has children
            chance *= (1 - (len(self.children) / maxChildren))
        if self.onMainPath is False:   # checks if this section is on the main path
            chance *= 0.5
        return chance

    def commitSection(self):        # adds the section to the map
        for key in self.sectionMap.keys():
            self.map.map[key] = self.sectionMap[key]
        if self.entrance[1] is not None:    #connect the section entrance to the previous section (if not the first section)
            prevRoom = self.map.map[self.entrance[0]].getNeighbourPosition(self.entrance[1])
            connectRooms(self.map.map[self.entrance[0]], self.map.map[prevRoom])

    def fill(self):          # generate the section
        done = False
        while random() <= self.newRoomChance():
            parentRoomPosition, parentRoomExit = self.getNextRoom(False)
            if parentRoomPosition is None:
                break
            self.addRoom(parentRoomPosition, parentRoomExit)
        self.writeSection()
        self.commitSection()
        while random() <= self.newChildChance() and self.map.sectionCount < maxSections and self.getUnassignedRooms() and self.roomCount() >= minSectionSize:
            parentRoomPosition, parentRoomExit = self.getNextRoom(True)
            if parentRoomPosition is not None:
                newSectionStart = self.sectionMap[parentRoomPosition].getNeighbourPosition(parentRoomExit)
                newSectionEntrance = inverseDir[parentRoomExit]
                if self.children or not self.onMainPath:
                    onMainPath = False
                else:
                    onMainPath = True
                self.map.sectionCount += 1
                self.children.append(Section(newSectionStart, newSectionEntrance, self.map.map, self.map, self.map.sectionCount - 1, self, onMainPath))
                self.map.sectionDict[self.children[-1].id] = self.children[-1]
                done = self.children[-1].fill()
            else:
                done = True
                break
        if not done:
            if self.map.sectionCount == maxSections:
                return True
            else:
                return False

    def getAvailableConnectionCount(self, room):  # return the number of connections the room has that a can lead to a new room
        count = 0
        for dir in room.connections.keys():
            if room.connections[dir] is False:
                pos = room.getNeighbourPosition(dir)
                if not pos in self.sectionMap and not pos in self.fullMap:
                    count += 1
        return count

    def getAvailableConnections(self, room):        # return the connections that can lead to a new room
        available = []
        for dir in room.connections.keys():             # iterate through the room's connections
            if room.connections[dir] is False:          # first check if a connection is unused
                pos = room.getNeighbourPosition(dir)
                if not pos in self.sectionMap and not pos in self.fullMap:  #then check if the adjacent room
                    available.append(dir)                                               #is empty
        if not available:
            return None
        else:
            return available

    def getNextRoom(self, useUnassignedPool):          # returns the room position and direction the next room will be generated from
        if useUnassignedPool:
            pool = self.getUnassignedRooms()
        else:
            pool = self.sectionMap.keys()
        possibleRooms = {}
        if pool:
            for id in pool:
                room = self.sectionMap[id]
                if self.getAvailableConnectionCount(room) > 0:
                    possibleRooms[room.xy] = self.getAvailableConnections(room)
        else:
            return None, None
        if possibleRooms:
            roomList = []
            for key in possibleRooms:
                roomList.append(key)
            parentRoom = choice(roomList)
            dir = choice(possibleRooms[parentRoom])
            return parentRoom, dir
        else:
            return None, None

    def addRoom(self, parentPosition, parentExit):      # adds a valid room to the section map
        parent = self.sectionMap[parentPosition]
        newPos = tuple((parent.xy[0] + dirOffset[parentExit][0], parent.xy[1] + dirOffset[parentExit][1]))
        newRoom = Room(newPos, parent.depth + 1, self.id)
        connectRooms(parent, newRoom)
        self.sectionMap[newRoom.xy] = newRoom

    def getRandomRoomID(self):
        return choice(list(self.sectionMap.keys()))

    def getUnassignedRooms(self):
        unassigned = []
        for room in list(self.sectionMap):
            if self.sectionMap[room].type is None:
                unassigned.append(room)
        if not unassigned:
            return False
        return unassigned

    def writeSection(self):
        f = open("section.txt" ,"a")
        for key in self.sectionMap.keys(): 
            output = str(key) + ": " + str(self.id) + "\n"
            f.write(output)
        f.close()







class Map:
    def __init__(self):
        self.map = {}   # dictionary to contain the rooms that are in the dungeon.
                        # rooms in here have been successfully placed on the map.
        self.sectionCount = 1
        self.firstSection = Section(tuple((0, 0)), None, self.map, self, 0, None, True)
        self.firstSection.sectionMap[tuple((0,0))].type = 'S'       #set start rooms type to S
        self.offsetVal = tuple((0, 0))     # set a default value for the offset for later
        self.size = tuple((0, 0))
        self.goalSection = -1
        self.sectionDict = {0: self.firstSection}
        self.passageInfo = []
        self.roomInfo = []
        self.availableKeys = deepcopy(keyBlocks)
        if not self.availableKeys:  # fills the list with temporary values if the list is empty
            c = 0
            while c < 48:
                self.availableKeys.append("temp#" + str(c))
                c += 1

    def createDungeon(self):            # Create the Structure of a maze
        self.firstSection.fill()

    def assignEmptyRooms(self):
        for roomID in list(self.map):
            room = self.map[roomID]
            if room.type is None or room.type == '0' or room.type == '1':
                room.type = choice(options)

    def setOffsetandSize(self):
        minx = 0
        maxx = 0
        miny = 0
        maxy = 0
        for key in self.map.keys():
            if key[0] < minx:
                minx = key[0]
            if key[0] > maxx:
                maxx = key[0]
            if key[1] < miny:
                miny = key[1]
            if key[1] > maxy:
                maxy = key[1]

        self.offsetVal = tuple((minx, maxy))
        self.size = tuple((maxx - minx + 1, maxy - miny + 1))
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def offset(self, pos):
        return tuple((pos[0] + self.offsetVal[0], -1 * (pos[1] + self.offsetVal[1])))

    def populateDungeon(self):
        self.setKeyRooms()
        self.assignEmptyRooms()

    def generateSectionPath(self):
        endID = self.getEndSectionID()
        path = []
        frontier = [self.firstSection.id]
        while frontier:
            next = frontier.pop(randrange(len(frontier)))
            path.append(next)
            for child in self.sectionDict[next].children:
                if child.id != endID:
                    frontier.append(child.id)
        path.append(endID)
        return path

    def getPassage(self, sectionID):
        sec = self.sectionDict[sectionID]
        pExit = sec.entrance[0]
        pDir = sec.entrance[1]
        pEnt = self.map[pExit].getNeighbourPosition(pDir)
        return pEnt, pExit




    def setKeyRooms(self):
        endID = self.getEndSectionID()
        self.map[self.sectionDict[endID].getRandomRoomID()].type = 'E'
        path = self.generateSectionPath()
        lastWasPuzzle = False
        while len(path) >= 2:
            if not lastWasPuzzle and len(path) > 2:
                roomType = randrange(2)
            else:
                roomType = 0
            if roomType == 0:       #if lever room is selected
                if self.sectionDict[path[0]].getUnassignedRooms():
                    keyRoom = self.map[choice(self.sectionDict[path[0]].getUnassignedRooms())]
                else:
                    keyRoom = self.map[self.sectionDict[path[0]].entrance[0]]
                keyRoom.type = 'K'
                keyRoom.meta = self.availableKeys.pop(randrange(len(self.availableKeys)))
                pEnt, pExit = self.getPassage(path[1])
                self.passageInfo.append([
                    "Key",
                    pEnt,
                    pExit,
                    keyRoom.meta
                ])
                lastWasPuzzle = False
            else:
                pEnt, pExit = self.getPassage(path[1])
                self.map[pEnt].type = 'P'
                self.passageInfo.append([
                    "Puzzle",
                    pEnt,
                    pExit
                    ])
                lastWasPuzzle = True
            path.pop(0)


    def getEndSectionID(self):
        section = self.firstSection
        while section.children:
            section = section.children[0]
        return section.id

    def writeDungeon(self):
        self.setOffsetandSize()
        textMap = ''
        y = self.maxy
        while y >= self.miny:
            x = self.minx
            southPassages = ''
            mid = ''
            bot = ''
            while x <= self.maxx:
                pos = tuple((x, y))
                if pos in self.map:
                    if self.map[pos].type is not None:
                        mid += str(self.map[pos].type)
                    else:
                        mid += str(self.map[pos].sectionID)
                    if self.map[pos].connections['e']:
                        mid += '-'
                    else:
                        mid += ' '
                    if self.map[pos].connections['s']:
                        bot += '| '
                    else:
                        bot += '  '

                    #print(x, ', ', y)
                    """
                    textMap += self.map[pos].type
                    if self.map[pos].connections['e'] is True:
                        textMap += '+'
                    else:
                        textMap += ' '
                    if self.map[pos].connections['s'] is True:
                        southPassages += '+ '
                    """
                else:
                    mid += '  '
                    bot += '  '
                    #textMap += '  '
                    #southPassages += '  '
                x += 1
            textMap += mid + '\n' + bot + '\n'
            y -= 1
        textMap += '***\n'
        for pi in self.passageInfo:
            i = 0
            for meta in pi:
                if i == 1 or i ==2:
                    textMap += str(useOffset(meta, self.offsetVal)) + ' '
                else:
                    textMap += str(meta) + ' '
                i += 1
            textMap += '\n'
        textMap += '***\n'
        for roomID in self.map:
            room = self.map[roomID]
            textMap += room.getMeta(self.offsetVal)
        return textMap






def areConnected(room1, room2):
    xy1 = room1.xy
    xy2 = room2.xy
    c1 = None
    c2 = None
    if xy1[0] == xy2[0]:            # if the rooms have the same x coordinate
        if xy1[1] - xy2[1] == 1:        # if room1 is 1 space above room2
            c1 = "s"
            c2 = "n"
        elif xy1[1] - xy2[1] == -1:     # if room1 is 1 space below room2
            c1 = "n"
            c2 = "s"
    elif xy1[1] == xy2[0]:           # if the rooms have the same y coordinate
        if xy1[1] - xy2[1] == 1:        # if room1 is 1 space right of room2
            c1 = "w"
            c2 = "e"
        elif xy1[1] - xy2[1] == -1:     # if room1 is 1 space left of room2
            c1 = "e"
            c2 = "w"
    if c1 is not None and c2 is not None:  # check that the rooms are next to each other
        if room1.connections[c1] is True and room2.connections[c2] is True:
            return True
    return False

def connectRooms(room1, room2):     # create a connection between two rooms and update their available connection count
    xy1 = room1.xy
    xy2 = room2.xy
    c1 = None
    c2 = None
    if xy1[0] == xy2[0]:            # if the rooms have the same x coordinate
        if xy1[1] - xy2[1] == 1:        # if room1 is 1 space above room2
            c1 = "s"
            c2 = "n"
        elif xy1[1] - xy2[1] == -1:     # if room1 is 1 space below room2
            c1 = "n"
            c2 = "s"
    elif xy1[1] == xy2[1]:           # if the rooms have the same y coordinate
        if xy1[0] - xy2[0] == 1:        # if room1 is 1 space right of room2
            c1 = "w"
            c2 = "e"
        elif xy1[0] - xy2[0] == -1:     # if room1 is 1 space left of room2
            c1 = "e"
            c2 = "w"
    if c1 is not None and c2 is not None:    # check that the room pair is valid
        room1.connections[c1] = True
        room2.connections[c2] = True
        room1.recalculateConnectionCount()
        room2.recalculateConnectionCount()
        return True
    print("Error: Unable to connect the following rooms:\t", xy1 , ' ', xy2)
    return False


def useOffset(tup, offset):
    return tuple((tup[0] - offset[0], -(tup[1] - offset[1])))


"""
# Populate the maze
def populateDungeon(dungeon):

    maxSectionDifficulty = ?
    for room in dungeon:
        RoomsSection = (getSection(room.sectionID))
        RoomToGenerate = random.choice(RoomsSectionTheme)
        while pass = 0:
            pass = 1
            RoomToGenerate = random.choice(RoomsSectionTheme)
            if RoomsSection.difficulty + RoomsSectionTheme[RoomToGenerate] > maxSectionDifficulty:
                pass = 0
                continue
            check other room requirements/generation requirements here:
                pass = 0
                continue



        
        



    
    
    
    
    
    test_output = ""
    for y in range(width):
        for x in range(length):
            # Do stuff instead of adding it to a string
            test_output += dungeon[x][y]
        test_output += "\n"
    print(test_output)
    return dungeon
    """
            
if __name__ == "__main__":
    minSectionSize = maxChildren + 3
    sectionCount = 0
    path = "map.txt"
    open('section.txt', 'w').close()
    print("Generating dungeon")
    dungeon = Map()
    dungeon.createDungeon()
    print("Dungeon generation complete")
    print("Assigning room types")
    dungeon.populateDungeon()
    print("Room type assignment complete")
    print("Converting dungeon to text")
    dungeonMap = dungeon.writeDungeon()
    print(dungeonMap)
    #dungeon = populateDungeon(dungeon)
    f = open("map.txt", "w")
    f.write(dungeonMap)
    f.close()