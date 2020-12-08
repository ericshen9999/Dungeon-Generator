options = [
    "S", # Start
    "E", # End
    "O", # Open Passage
    "B", # Button
    "L", # Lever
    "P", # Puzzle
    "R", # Room
    "T", # Trapped Room
    "F", # Fake Room
    " " # Nothing
]
# 3 x 3 (*2 for passageways -1 for edges)
length = 3 * 2 - 1
width = 3 * 2 - 1

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