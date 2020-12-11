# File Input -----------------
datafile = open("d11.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def updateGrid(data):
    row = len(data)
    col = len(data[0])
    updated = False
    # new empty grid to update
    newgrid = [[None for i in range(col)] for j in range(row)]

    for y in range(row):
        for x in range(col):
            if data[y][x] == ".":
                newgrid[y][x] == "."
            else:
                adjacentFilled = 0
                # seat coords:
                # [-1,-1][0,-1][1,-1]
                # [-1,0 ][0,0] [1,0 ]
                # [-1,1 ][0,1] [1,1 ]
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == dx == 0:
                            continue

                        yy = y + dy
                        xx = x + dx
                        if(not 0 <= yy < row) or (not 0 <= xx < col):
                            continue
                        if data[yy][xx] == "#":
                            adjacentFilled += 1

                if data[y][x] == "L" and adjacentFilled == 0:
                    updated = True
                    newgrid[y][x] = "#"
                elif data[y][x] == "#" and adjacentFilled >= 4:
                    updated = True
                    newgrid[y][x] = "L"
                else:
                    newgrid[y][x] = data[y][x]
    return newgrid, updated

def filledCount(data):
    c = 0
    for i in data:
        for j in i:
            if j == "#":
                c += 1
    return c

updated = True
while updated:
    data, updated = updateGrid(data)

print(filledCount(data))