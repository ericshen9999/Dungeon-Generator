from random import choice

# Rooms are 11x11 with 9x9 insides (+10 for the next room since walls overlap)
# (x,z,y) [-100, 3, 120]
def generateRoom(x,y,z,block):
    commandlist = []
    command = "/fill " + str(x) + " " + str(y) + " " + str(z) + " " + str(x+10) + " " + str(y+3) + " " + str(z+10) + " minecraft:" + block + " keep"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y+1) + " " + str(z+1) + " " + str(x+9) + " " + str(y+3) + " " + str(z+9) + " minecraft:air replace minecraft:" + block
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
def generateLockedDoor(x,y,z,direction,block):
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

def generateDoor(x,y,z,direction):
    commandlist = []
    dis = dirDic[direction]
    command = "/setblock " + str(x + dis[0]) + " " + str(y + 1) + " " + str(z + dis[1]) + " minecraft:air"
    commandlist.append(command)
    command = "/setblock " + str(x + dis[0]) + " " + str(y + 2) + " " + str(z + dis[1]) + " minecraft:air"
    commandlist.append(command)
    return commandlist

def get3x3(x,y,z,block):
    commandlist = []
    command = "/fill " + str(x+1) + " " + str(y-1) + " " + str(z+1) + " " + str(x+9) + " " + str(y-6) + " " + str(z+9) + " minecraft:air replace"
    commandlist.append(command)

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

    command = "/fill " + str(x+2) + " " + str(y+1) + " " + str(z+4) + " " + str(x+2) + " " + str(y+1) + " " + str(z+6) + " " + block + " replace"
    commandlist.append(command)
    command = "/fill " + str(x+8) + " " + str(y+1) + " " + str(z+4) + " " + str(x+8) + " " + str(y+1) + " " + str(z+6) + " " + block + " replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+1) + " " + str(z+2) + " " + str(x+6) + " " + str(y+1) + " " + str(z+2) + " " + block + " replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y+1) + " " + str(z+8) + " " + str(x+6) + " " + str(y+1) + " " + str(z+8) + " " + block + " replace"
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

def getTape(x,y,z,block):
    commandlist = []
    command = "/fill " + str(x+1) + " " + str(y-1) + " " + str(z+1) + " " + str(x+9) + " " + str(y-6) + " " + str(z+9) + " minecraft:air replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y) + " " + str(z+1) + " " + str(x+6) + " " + str(y) + " " + str(z+9) + " minecraft:barrier replace"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y) + " " + str(z+4) + " " + str(x+9) + " " + str(y) + " " + str(z+6) + " minecraft:barrier replace"
    commandlist.append(command)

    command = "/setblock " + str(x+4) + " " + str(y) + " " + str(z+4) + " minecraft:red_stained_glass replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y) + " " + str(z+4) + " minecraft:red_stained_glass replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y) + " " + str(z+6) + " minecraft:red_stained_glass replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y) + " " + str(z+6) + " minecraft:red_stained_glass replace"
    commandlist.append(command)

    command = "/setblock " + str(x+8) + " " + str(y+1) + " " + str(z+9) + " minecraft:stone_button[face=floor, facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y+1) + " " + str(z+8) + " minecraft:stone_button[face=floor, facing=north] replace"
    commandlist.append(command)

    command = "/fill " + str(x+5) + " " + str(y-1) + " " + str(z+1) + " " + str(x+6) + " " + str(y-1) + " " + str(z+1) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-1) + " " + str(z+2) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y-1) + " " + str(z+4) + " " + str(x+1) + " " + str(y-1) + " " + str(z+5) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y-1) + " " + str(z+7) + " " + str(x+3) + " " + str(y-1) + " " + str(z+7) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+9) + " " + str(y-1) + " " + str(z+5) + " " + str(x+9) + " " + str(y-1) + " " + str(z+6) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+9) + " " + str(x+5) + " " + str(y-1) + " " + str(z+9) + " minecraft:black_concrete replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-1) + " " + str(z+2) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-1) + " " + str(z+3) + " " + str(x+4) + " " + str(y-1) + " " + str(z+7) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+6) + " " + str(y-1) + " " + str(z+3) + " " + str(x+6) + " " + str(y-1) + " " + str(z+8) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(y-1) + " " + str(z+4) + " " + str(x+6) + " " + str(y-1) + " " + str(z+4) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-1) + " " + str(z+5) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(y-1) + " " + str(z+6) + " " + str(x+6) + " " + str(y-1) + " " + str(z+6) + " minecraft:white_concrete replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-1) + " " + str(z+8) + " minecraft:white_concrete replace"
    commandlist.append(command)

    command = "/fill " + str(x+7) + " " + str(y-1) + " " + str(z+4) + " " + str(x+8) + " " + str(y-1) + " " + str(z+4) + " minecraft:redstone_block replace"
    commandlist.append(command)
    command = "/setblock " + str(x+8) + " " + str(y-1) + " " + str(z+5) + " minecraft:redstone_block replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-1) + " " + str(z+6) + " minecraft:redstone_block replace"
    commandlist.append(command)

    command = "/setblock " + str(x+4) + " " + str(y-1) + " " + str(z+1) + " minecraft:piston[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-1) + " " + str(z+2) + " minecraft:piston[facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-1) + " " + str(z+3) + " minecraft:piston[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-1) + " " + str(z+4) + " minecraft:piston[facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+1) + " " + str(y-1) + " " + str(z+6) + " minecraft:piston[facing=east] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+8) + " " + str(y-1) + " " + str(z+7) + " minecraft:piston[facing=south] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-1) + " " + str(z+8) + " minecraft:piston[facing=south] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-1) + " " + str(z+8) + " minecraft:piston[facing=east] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-1) + " " + str(z+9) + " minecraft:piston[facing=south] replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y-2) + " " + str(z+1) + " " + str(x+6) + " " + str(y-2) + " " + str(z+3) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+1) + " " + str(y-2) + " " + str(z+5) + " " + str(x+3) + " " + str(y-2) + " " + str(z+6) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-2) + " " + str(z+4) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-2) + " " + str(z+5) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+7) + " " + str(y-2) + " " + str(z+5) + " " + str(x+8) + " " + str(y-2) + " " + str(z+6) + " minecraft:black_concrete replace"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(y-2) + " " + str(z+7) + " " + str(x+6) + " " + str(y-2) + " " + str(z+9) + " minecraft:black_concrete replace"
    commandlist.append(command)

    command = "/setblock " + str(x+9) + " " + str(y-2) + " " + str(z+4) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+8) + " " + str(y-2) + " " + str(z+9) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-2) + " " + str(z+8) + " minecraft:sticky_piston[facing=south] replace"
    commandlist.append(command)

    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+1) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-2) + " " + str(z+2) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-2) + " " + str(z+2) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-2) + " " + str(z+3) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-2) + " " + str(z+3) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-2) + " " + str(z+4) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-2) + " " + str(z+5) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-2) + " " + str(z+6) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+1) + " " + str(y-2) + " " + str(z+6) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+7) + " minecraft:observer[facing=up] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+8) + " " + str(y-2) + " " + str(z+7) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-2) + " " + str(z+7) + " minecraft:observer[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-2) + " " + str(z+8) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)

    command = "/setblock " + str(x+8) + " " + str(y-1) + " " + str(z+9) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+1) + " minecraft:piston[facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-3) + " " + str(z+3) + " minecraft:piston[facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-3) + " " + str(z+3) + " minecraft:piston[facing=south] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+1) + " " + str(y-3) + " " + str(z+5) + " minecraft:piston[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+3) + " " + str(y-3) + " " + str(z+7) + " minecraft:piston[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-3) + " " + str(z+7) + " minecraft:piston[facing=east] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+8) + " " + str(y-3) + " " + str(z+9) + " minecraft:piston[facing=west] replace"
    commandlist.append(command)
    
    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+2) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+6) + " " + str(y-3) + " " + str(z+3) + " " + str(x+6) + " " + str(y-3) + " " + str(z+4) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+3) + " " + str(y-3) + " " + str(z+4) + " " + str(x+4) + " " + str(y-3) + " " + str(z+4) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+2) + " " + str(y-3) + " " + str(z+5) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-3) + " " + str(z+5) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+4) + " " + str(y-3) + " " + str(z+6) + " " + str(x+4) + " " + str(y-3) + " " + str(z+7) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/fill " + str(x+6) + " " + str(y-3) + " " + str(z+6) + " " + str(x+7) + " " + str(y-3) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+6) + " minecraft:redstone_wall_torch[facing=east] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-3) + " " + str(z+5) + " minecraft:redstone_wall_torch[facing=south] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+4) + " minecraft:redstone_wall_torch[facing=west] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-3) + " " + str(z+5) + " minecraft:redstone_wall_torch[facing=north] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+7) + " " + str(y-3) + " " + str(z+9) + " minecraft:observer[facing=down] replace"
    commandlist.append(command)

    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+4) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+4) + " " + str(y-2) + " " + str(z+6) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-2) + " " + str(z+4) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+6) + " " + str(y-2) + " " + str(z+6) + " minecraft:redstone_wire[east=none, north=none, south=none, west=none] replace"
    commandlist.append(command)
    command = "/setblock " + str(x+9) + " " + str(y-2) + " " + str(z+5) + " minecraft:redstone_wire[east=side, north=side, south=side, west=side] replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y-5) + " " + str(z+4) + " " + str(x+6) + " " + str(y-5) + " " + str(z+6) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/fill " + str(x+4) + " " + str(y-4) + " " + str(z+4) + " " + str(x+6) + " " + str(y-4) + " " + str(z+6) + " minecraft:redstone_wire replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-4) + " " + str(z+5) + " minecraft:air replace"
    commandlist.append(command)

    command = "/fill " + str(x+5) + " " + str(y-5) + " " + str(z+7) + " " + str(x+5) + " " + str(y-5) + " " + str(z+9) + " minecraft:stone_bricks replace"
    commandlist.append(command)

    command = "/fill " + str(x+5) + " " + str(y-4) + " " + str(z+7) + " " + str(x+5) + " " + str(y-4) + " " + str(z+9) + " minecraft:redstone_wire replace"
    commandlist.append(command)

    command = "/setblock " + str(x+5) + " " + str(y-4) + " " + str(z+10) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-3) + " " + str(z+10) + " minecraft:redstone_torch replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-2) + " " + str(z+10) + " minecraft:stone_bricks replace"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y-1) + " " + str(z+10) + " minecraft:redstone_torch replace"
    commandlist.append(command)

    return commandlist

puzzleType = {
    "3x3": get3x3,
    "Tape": getTape
}

# (x,y,z,direction,block) [-100, 3, 120, "north", "white_wool"]
def findPuzzle(x,y,z,name,block):
    if name in puzzleType:
        return puzzleType[name](x,y,z,block)
    else:
        print("ERROR:", x, ",", y, ",", z, ",", name, "not found")
        return None

def getKeyRoom(x,y,z,block):
    commandlist = []
    command = "/setblock " + str(x+5) + " " + str(y) + " " + str(z+5) + " minecraft:command_block{{}Command:\"/give @p minecraft:lever{CanPlaceOn:[" + "'" + "minecraft:" + block + "']{}}\"} destroy"
    commandlist.append(command)
    command = "/setblock " + str(x+5) + " " + str(y+1) + " " + str(z+5) + " minecraft:stone_pressure_plate"
    commandlist.append(command)
    return commandlist

def getSection(localx, localy):
    search = "(" + str(localx) + ", " + str(localy) + ")"
    with open("section.txt", "r") as f:
        for line in f:
            if search in line:
                return line[-2:-1]

roomType = { # Can be randomized later
    "0": "netherrack",
    "1": "stone", #Section 1 is Stone (can be changed)
    "2": "cobblestone",
    "3": "iron_block",
    "4": "sandstone",
    "5": "ice",
    "6": "slime_block",
    "7": "end_stone",
    "8": "purpur_block",
    "9": "quartz_block"
}
def getBlock(section):
    return roomType[section]


def getStart(x,y,z,block):
    commandlist = ["/setblock " + str(x+5) + " " + str(y+1) + " " + str(z+5) + " minecraft:oak_sign[rotation=0]{{}Text1:\"\\\"Start\\\"\"{}}"]
    return generateRoom(x,y,z,block) + commandlist
def getEnd(x,y,z,block):
    commandlist = ["/setblock " + str(x+5) + " " + str(y+1) + " " + str(z+5) + " minecraft:oak_sign[rotation=0]{{}Text1:\"\\\"End\\\"\"{}}"]
    return generateRoom(x,y,z,block) + commandlist
def getRoom(x,y,z,block):
    return generateRoom(x,y,z,block)
def getKey(x,y,z,block,keyblock):
    return generateRoom(x,y,z,block) + getKeyRoom(x,y,z,keyblock)
def getPuzzle(x,y,z,block):
    return generateRoom(x,y,z,block) + findPuzzle(x,y,z,choice(list(puzzleType.keys())),block)

# Where the start block is
# /setblock x y+4 z minecraft:pink_carpet

roomFunction = {
    "S": getStart, #x,y,z,block
    "E": getEnd, #x,y,z,block
    "R": getRoom, #x,y,z,block
    "K": getKey, #x,y,z,block,keyblock
    "P": getPuzzle, #x,y,z,block
    "|": generateDoor, #x,y,z,direction
    "-": generateDoor #x,y,z,direction
    #"L": generateLockedDoor #x,y,z,direction,keyblock
}
if __name__ == "__main__":
    # Test location (-100, 3, 120)
    #localx = 0
    #localy = 0
    #absolutex = localx * 11
    #absolutey = 3
    #absolutez = localy * 11
    #block = roomType[getSection(localx,localy)]
    #f = open("commands.txt", "w")
    #for command in getStart(absolutex,absolutey,absolutez,block):
        #f.write(command + "\n")
    #f.close()

    currxf = 0.0
    curry = 12
    currzf = 0.0
    stage = 1

    comf = open("commands.txt", "w")
    with open("map.txt") as mapf:
        for line in mapf:
            for c in line:

                if stage == 1:
                    currx = int(currxf)
                    currz = int(currzf)
                    if c == '*':
                        stage = 2
                        break
                    if c == 'S':
                        for command in getStart((10 * currx), (curry), (10 * currz),
                                                                                    getBlock(getSection(currx, currz))):
                            comf.write(command + "\n")
                    if c == 'E':
                        for command in getEnd((10 * currx), (curry), (10 * currz),
                                                                                    getBlock(getSection(currx, currz))):
                            comf.write(command + "\n")
                    if c == 'R':
                        for command in getRoom((10 * currx), (curry), (10 * currz),
                                                                                    getBlock(getSection(currx, currz))):
                            comf.write(command + "\n")
                    if c == 'P':
                        for command in getPuzzle((10 * currx), (curry), (10 * currz),
                                                                                    getBlock(getSection(currx, currz))):
                            comf.write(command + "\n")
                    currxf += 0.5

                if stage == 2:
                    if c == '*':
                        stage = 3
                        break

                if stage == 3:
                    break
            currxf = 0
            currzf += 0.5

    comf.close()