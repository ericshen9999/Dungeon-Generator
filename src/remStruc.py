if __name__ == "__main__":
    currxf = 0.0
    curry = 12
    currzf = 0.0
    stage = 1

    comf = open("commands.txt", "w")
    with open("map.txt") as mapf:
        for line in mapf:
            for c in line:

                if stage == 1:
                    currx = int(currxf) * 10
                    currz = int(currzf) * 10
                    if c == '*':
                        stage = 2
                        break
                    if c == 'S':
                        command = "/fill " + str(currx) + " " + str(curry) + " " + str(currz) + " " + str(
                            currx + 10) + " " + str(curry + 3) + " " + str(currz + 10) + " minecraft:air replace"
                        comf.write(command + "\n")
                    if c == 'E':
                        command = "/fill " + str(currx) + " " + str(curry) + " " + str(currz) + " " + str(
                            currx + 10) + " " + str(curry + 3) + " " + str(currz + 10) + " minecraft:air replace"
                        comf.write(command + "\n")
                    if c == 'R':
                        command = "/fill " + str(currx) + " " + str(curry) + " " + str(currz) + " " + str(
                            currx + 10) + " " + str(curry + 3) + " " + str(currz + 10) + " minecraft:air replace"
                        comf.write(command + "\n")
                    if c == 'P':
                        command = "/fill " + str(currx) + " " + str(curry - 6) + " " + str(currz) + " " + str(
                            currx + 10) + " " + str(curry + 3) + " " + str(currz + 10) + " minecraft:air replace"
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