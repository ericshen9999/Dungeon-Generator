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

if __name__ == "__main__":
    # Test location (-100, 3, 120)
    print(generateDoor(-100, 3, 120, "west","white_wool"))