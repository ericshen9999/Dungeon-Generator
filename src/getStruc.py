# Rooms are 11x11 with 9x9 insides (+10 for the next room since walls overlap)
# (x,z,y) [-100, 3, 120]
def generateRoom(x,y,z):
    commandlist = []
    command = "/fill " + str(x) + " " + str(y) + " " + str(z) + " " + str(x+10) + " " + str(y+3) + " " + str(z+10) + " minecraft:stone_bricks keep"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y+1) + " " + str(z+1) + " " + str(x+9) + " " + str(y+3) + " " + str(z+9) + " minecraft:air replace minecraft:stone_bricks"
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
def generateDoor(x,y,z,direction,block):
    commandlist = []
    dis = dirDic[direction]
    dis2 = dirDic2[direction]
    command = "/setblock " + str(x + dis[0]) + " " + str(y + 1) + " " + str(z + dis[1]) + " minecraft:iron_door[half=lower, facing=" + inverseDir[direction] + "]"
    commandlist.append(command)
    command = "/setblock " + str(x + dis[0]) + " " + str(y + 2) + " " + str(z + dis[1]) + " minecraft:iron_door[half=upper, facing=" + inverseDir[direction] + "]"
    commandlist.append(command)
    command = "/setblock " + str(x + dis[0] + dis2[0]) + " " + str(y + 2) + " " + str(z + dis[1] + dis2[1]) + " minecraft:" + block
    commandlist.append(command)
    return commandlist


def get3x3(x,y,z):
    commandlist = []
    command = "/fill " + str(x+4) + " " + str(y) + " " + str(z+4) + " " + str(x+6) + " " + str(y) + " " + str(z+6) + " minecraft:barrier replace"
    commandlist.append(command)

    command = "/fill " + str(x+1) + " " + str(y-1) + " " + str(z+1) + " " + str(x+9) + " " + str(y-1) + " " + str(z+9) + " minecraft:obsidian replace"
    commandlist.append(command)
    command = "/fill " + str(x+2) + " " + str(y-1) + " " + str(z+2) + " " + str(x+8) + " " + str(y-1) + " " + str(z+8) + " minecraft:air replace minecraft:obsidian"
    commandlist.append(command)

    command = "/fill " + str(x+2) + " " + str(y-1) + " " + str(z+4) + " " + str(x+2) + " " + str(y-1) + " " + str(z+6) + " minecraft:sticky_piston[facing=down] replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y-1) + " " + str(z+4) + " " + str(x+8) + " " + str(y-1) + " " + str(z+6) + " minecraft:sticky_piston[facing=down] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+2) + " " + str(x+6) + " " + str(y-1) + " " + str(z+2) + " minecraft:sticky_piston[facing=down] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+8) + " " + str(x+6) + " " + str(y-1) + " " + str(z+8) + " minecraft:sticky_piston[facing=down] replace"
    commandlist.append(command)

    command = "/fill " + str(x+2) + " " + str(y) + " " + str(z+4) + " " + str(x+2) + " " + str(y) + " " + str(z+6) + " minecraft:powered_rail replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y) + " " + str(z+4) + " " + str(x+8) + " " + str(y) + " " + str(z+6) + " minecraft:powered_rail replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y) + " " + str(z+2) + " " + str(x+6) + " " + str(y) + " " + str(z+2) + " minecraft:powered_rail replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y) + " " + str(z+8) + " " + str(x+6) + " " + str(y) + " " + str(z+8) + " minecraft:powered_rail replace"
    commandlist.append(command)

    command = "/fill " + str(x+3) + " " + str(y-1) + " " + str(z+4) + " " + str(x+3) + " " + str(y-1) + " " + str(z+6) + " minecraft:sticky_piston[facing=north] replace"
    commandlist.append(command)
    command = "/fill " + str(x+7) + " " + str(y-1) + " " + str(z+4) + " " + str(x+7) + " " + str(y-1) + " " + str(z+6) + " minecraft:sticky_piston[facing=south] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+3) + " " + str(x+6) + " " + str(y-1) + " " + str(z+3) + " minecraft:sticky_piston[facing=west] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+7) + " " + str(x+6) + " " + str(y-1) + " " + str(z+7) + " minecraft:sticky_piston[facing=east] replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+5) + " " + str(x+4) + " " + str(y-1) + " " + str(z+6) + " minecraft:smooth_quartz replace"
    commandlist.append(command)
    command = "/fill " + str(x+6) + " " + str(y-1) + " " + str(z+5) + " " + str(x+6) + " " + str(y-1) + " " + str(z+6) + " minecraft:smooth_quartz replace"
    commandlist.append(command)
    command = "/fill " + str(x+5) + " " + str(y-1) + " " + str(z+4) + " " + str(x+5) + " " + str(y-1) + " " + str(z+6) + " minecraft:redstone_block replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-1) + " " + str(z+4) + " minecraft:redstone_block replace"
    commandlist.append(command)

    command = "/fill " + str(x+2) + " " + str(y-2) + " " + str(z+4) + " " + str(x+2) + " " + str(y-2) + " " + str(z+6) + " minecraft:observer[facing=south] replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y-2) + " " + str(z+4) + " " + str(x+8) + " " + str(y-2) + " " + str(z+6) + " minecraft:observer[facing=north] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-2) + " " + str(z+2) + " " + str(x+6) + " " + str(y-2) + " " + str(z+2) + " minecraft:observer[facing=east] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-2) + " " + str(z+8) + " " + str(x+6) + " " + str(y-2) + " " + str(z+8) + " minecraft:observer[facing=west] replace"
    commandlist.append(command)

    command = "/fill " + str(x+3) + " " + str(y-2) + " " + str(z+4) + " " + str(x+3) + " " + str(y-2) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+7) + " " + str(y-2) + " " + str(z+4) + " " + str(x+7) + " " + str(y-2) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-2) + " " + str(z+3) + " " + str(x+6) + " " + str(y-2) + " " + str(z+3) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-2) + " " + str(z+7) + " " + str(x+6) + " " + str(y-2) + " " + str(z+7) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/setblock " + str(x+4) + " " + str(y-3) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-3) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-3) + " " + str(z+4) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-3) + " " + str(z+4) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+6) + " minecraft:redstone_wall_torch[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-3) + " " + str(z+5) + " minecraft:redstone_wall_torch[facing=east] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+4) + " minecraft:redstone_wall_torch[facing=south] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-3) + " " + str(z+5) + " minecraft:redstone_wall_torch[facing=west] replace"
    commandlist.append(command)
    
    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+6) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-2) + " " + str(z+6) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-2) + " " + str(z+4) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+4) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)

    
    command = "/fill " + str(x+4) + " " + str(y-5) + " " + str(z+4) + " " + str(x+6) + " " + str(y-5) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y-4) + " " + str(z+4) + " " + str(x+6) + " " + str(y-4) + " " + str(z+6) + " minecraft:redstone_wire replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-4) + " " + str(z+5) + " minecraft:air replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-5) + " " + str(z+7) + " minecraft:redstone_wall_torch[facing=west] replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-6) + " " + str(z+8) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-5) + " " + str(z+9) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-4) + " " + str(z+10) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-2) + " " + str(z+10) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-5) + " " + str(z+8) + " minecraft:redstone_wire replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-4) + " " + str(z+9) + " minecraft:redstone_wire replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+10) + " minecraft:redstone_torch replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-1) + " " + str(z+10) + " minecraft:redstone_torch replace"
    commandlist.append(command)

    command = "/fill " + str(x+2) + " " + str(y+1) + " " + str(z+4) + " " + str(x+2) + " " + str(y+1) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y+1) + " " + str(z+4) + " " + str(x+8) + " " + str(y+1) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+1) + " " + str(z+2) + " " + str(x+6) + " " + str(y+1) + " " + str(z+2) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+1) + " " + str(z+8) + " " + str(x+6) + " " + str(y+1) + " " + str(z+8) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    
    command = "/fill " + str(x+2) + " " + str(y+2) + " " + str(z+4) + " " + str(x+2) + " " + str(y+2) + " " + str(z+6) + " minecraft:stone_button[face=floor, facing=south] replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y+2) + " " + str(z+4) + " " + str(x+8) + " " + str(y+2) + " " + str(z+6) + " minecraft:stone_button[face=floor, facing=north] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+2) + " " + str(z+2) + " " + str(x+6) + " " + str(y+2) + " " + str(z+2) + " minecraft:stone_button[face=floor, facing=east] replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+2) + " " + str(z+8) + " " + str(x+6) + " " + str(y+2) + " " + str(z+8) + " minecraft:stone_button[face=floor, facing=west] replace"
    commandlist.append(command)

    return commandlist

puzzleType = {
    "3x3": get3x3
}
# (x,y,z,direction,block) [-100, 3, 120, "north", "white_wool"]
def getpuzzle(x,y,z,name):
    if name in puzzleType:
        return puzzleType[name](x,y,z)
    else:
        print("ERROR:", x, ",", y, ",", z, ",", name, "not found")
        return None
    
# Where the start block is
# /setblock x y+4 z minecraft:pink_carpet

if __name__ == "__main__":
    # Test location (-100, 3, 120)
    print(getpuzzle(-100,3,120,"3x3"))