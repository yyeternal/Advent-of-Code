filepath = "C:\\Users\\jtint\\OneDrive\\Documents\\Advent\\inputday5.txt"
def doCoolStuff():
    with open("inputday5.txt", "r") as file:
        lines = file.readlines()
        seeds = []
        temp = lines[0].split()
        temp.pop(0)
        maps = [[], [], [], [], [], [], []]
        mapIndex = -1
        for line in lines[1:]:
            if line == '\n':
                mapIndex += 1
            else:
                elts = line.split()
                if elts[0].isnumeric():
                    elts = [int(i) for i in elts]
                    maps[mapIndex].append(elts)
        arrays = []
        temp = [int(i) for i in temp]
        for i in range (0, len(temp)):
            seeds.append(temp[i])
        for seed in seeds:
            arrays.append(findIfInRange(seed,maps))
            arrays.sort()
        print(arrays[0])


def findIfInRange(seed, maps):
    location = seed
    for map in maps:
        for i in range(len(map)):
            value = abs(location - map[i][1])
            if map[i][1] <= location and value < map[i][2]:
                location = map[i][0] + value
                break
    return location
               
doCoolStuff()