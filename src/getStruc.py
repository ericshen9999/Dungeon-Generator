# Rooms are 11x11 with 9x9 insides (+10 for the next room since walls overlap)
# (x,z,y) [-100, 3, 120]
def generateRoom(x,z,y):
    commandlist = []
    command = "/fill " + str(x) + " " + str(z) + " " + str(y) + " " + str(x+10) + " " + str(z+3) + " " + str(y+10) + " minecraft:stone keep"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(z+1) + " " + str(y+1) + " " + str(x+9) + " " + str(z+3) + " " + str(y+9) + " minecraft:air replace minecraft:stone"
    commandlist.append(command)
    return commandlist
# For Door
dirDic = {
    "north": (5,10),
    "south": (5,0),
    "east": (0,5),
    "west": (10,5)
}
# For Block
dirDic2 = {
    "north": (-1,0),
    "south": (1,0),
    "east": (0,-1),
    "west": (0,1)
}
# For Door Facing
inverseDir = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east"
}
# (x,z,y,direction,block) [-100, 3, 120, "north", "white_wool"]
def generateDoor(x,z,y,direction,block):
    commandlist = []
    dis = dirDic[direction]
    dis2 = dirDic2[direction]
    command = "/setblock " + str(x + dis[0]) + " " + str(z + 1) + " " + str(y + dis[1]) + " minecraft:iron_door[half=lower, facing=" + inverseDir[direction] + "]"
    commandlist.append(command)
    command = "/setblock " + str(x + dis[0]) + " " + str(z + 2) + " " + str(y + dis[1]) + " minecraft:iron_door[half=upper, facing=" + inverseDir[direction] + "]"
    commandlist.append(command)
    command = "/setblock " + str(x + dis[0] + dis2[0]) + " " + str(z + 2) + " " + str(y + dis[1] + dis2[1]) + " minecraft:" + block
    commandlist.append(command)
    return commandlist


def get3x3(x,z,y):
    commandlist = []
    command = "/fill " + str(x+4) + " " + str(z) + " " + str(y+4) + " " + str(x+6) + " " + str(z) + " " + str(y+6) + " minecraft:barrier replace"
    commandlist.append(command)
    command = "/fill " + str(x+2) + " " + str(z-1) + " " + str(y+2) + " " + str(x+8) + " " + str(z-1) + " " + str(y+8) + " minecraft:obsidian replace"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(z-1) + " " + str(y+3) + " " + str(x+7) + " " + str(z-1) + " " + str(y+7) + " minecraft:air replace minecraft:obsidian"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(z-1) + " " + str(y+4) + " " + str(x+3) + " " + str(z-1) + " " + str(y+6) + " minecraft:sticky_piston[facing=east]"
    commandlist.append(command)
    command = "/fill " + str(x+7) + " " + str(z-1) + " " + str(y+4) + " " + str(x+7) + " " + str(z-1) + " " + str(y+6) + " minecraft:sticky_piston[facing=west]"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(z-1) + " " + str(y+3) + " " + str(x+6) + " " + str(z-1) + " " + str(y+3) + " minecraft:sticky_piston[facing=south]"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(z-1) + " " + str(y+7) + " " + str(x+6) + " " + str(z-1) + " " + str(y+7) + " minecraft:sticky_piston[facing=north]"
    commandlist.append(command)
    return commandlist

puzzleType = {
    "3x3": get3x3
}
# (x,z,y,direction,block) [-100, 3, 120, "north", "white_wool"]
def getpuzzle(x,z,y,name):
    if name in puzzleType:
        return puzzleType[name](x,z,y)
    else:
        print("ERROR:", x, ",", y, ",", z, ",", name, "not found")
        return None
    
# Where the start block is
# /setblock x y+4 z minecraft:pink_carpet

if __name__ == "__main__":
    # Test location (-100, 3, 120)
    print(getpuzzle(-100,3,120,"3x3"))