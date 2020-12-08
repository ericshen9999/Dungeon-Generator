
if __name__ == "__main__":
    path = "map.txt"
    dungeon = createMaze();
    f = open(path)
    f.write(dungeon)
    f.close()
    
def createMaze():
    