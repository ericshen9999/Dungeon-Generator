from random import choice, choices
options = [
    "S",    # Start
    "E",    # End
    "O",    # Open Passage
    "B",    # Button
    "L",    # Lever
    "P",    # Puzzle
    "R",    # Room
    "T",    # Trapped Room
    "F",    # Fake Room
    " "     # Nothing
]

maxSections = 10        #maximum number of sections the dungeon can have
maxSectionSize = 10     #maximum number of rooms a section can have
maxChildren = 1         # Maximum number of children a section can have

inverseDir = {   #just a dictionary for quickly getting an opposite direction
    "n": "s",
    "e": "w",
    "s": "n",
    "w": "e"
}
# 3 x 3 (*2 for passageways -1 for edges)
length = 3 * 2 - 1
width = 3 * 2 - 1


class Room:         #Class for a single room
    def __init__(self, xy, depth):
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
    def recalculateConnectionCount(self):
        self.connectionNum = 0
        for val in self.connections:
            if val is True:
                self.connectionNum += 1
class Section:      #Class for a section - a connected set of rooms
    def __init__(self, entrancePos, entranceDir, currentGrid):      #passes the entrance position, entrance direction
                                                                    # and a dictionary positions already in use
        self.children = []                  # A list of children sections.  Should only be added to after the section
                                            # has finished generating its rooms
        self.prefilled = currentGrid        # might not be needed, may remove later
        self.sectionMap = {entrancePos: Room(entrancePos, 0)}  # the map of rooms in this section
        if entranceDir is not None:     #only execute the next lines if this isn't the first section
            self.sectionMap[entrancePos].connections[inverseDir[entranceDir]] = True # set the initial room in the
                                                                                     # section to be connected
            self.sectionMap[entrancePos].recalculateConnectionCount()

class Map:
    def __init__(self):
        self.map = {}   # dictionary to contain the rooms that are in the dungeon.
                        # rooms in here have been successfully placed on the map.
        self.firstSection = Section((0, 0), None, self.map)

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
    elif xy1[1] == xy2[0]:           # if the rooms have the same y coordinate
        if xy1[1] - xy2[1] == 1:        # if room1 is 1 space right of room2
            c1 = "w"
            c2 = "e"
        elif xy1[1] - xy2[1] == -1:     # if room1 is 1 space left of room2
            c1 = "e"
            c2 = "w"
    if c1 is not None and c2 is not None:    # check that the room pair is valid
        room1.connections[c1] = True
        room2.connections[c2] = True
        room1.recalculateConnectionCount()
        room2.recalculateConnecitonCount()
        return True
    print("Error: Unable to connect the following rooms:\t" + xy1 + xy2)
    return False

# Create the Structure of a maze 
def createDungeon():
    # [x][y]
    dungeon = [[" " for x in range(length)] for y in range(width)] 
    # (x,y)
    currentpos = (0, 0)
    dungeon[currentpos[0]][currentpos[1]] = "S"

    # Use +-2 to check for room rather than passage way                     # Need to implement randomness and likely a queue
    if currentpos[0] + 2 < length:
        # Can go right
        if dungeon[currentpos[0] + 2][currentpos[1]] == " ":
            # Empty room is found, continue on
            pass
    if currentpos[1] + 2 < width:
        # Can go up
        if dungeon[currentpos[0]][currentpos[1] + 2] == " ":
            # Empty room is found, continue on
            pass
    if currentpos[0] - 2 > 0:
        # Can go left
        if dungeon[currentpos[0] - 2][currentpos[1]] == " ":
            # Empty room is found, continue on
            pass
    if currentpos[1] - 2 > 0:
        # Can go down
        if dungeon[currentpos[0]][currentpos[1] - 2] == " ":
            # Empty room is found, continue on
            pass
    return dungeon
# Populate the maze
def populateDungeon(dungeon):
    test_output = ""
    for y in range(width):
        for x in range(length):
            # Do stuff instead of adding it to a string
            test_output += dungeon[x][y]
        test_output += "\n"
    print(test_output)
    return dungeon
            
if __name__ == "__main__":
    path = "map.txt"
    dungeon = createDungeon()
    dungeon = populateDungeon(dungeon)
    f = open(path)
    f.write(dungeon)
    f.close()