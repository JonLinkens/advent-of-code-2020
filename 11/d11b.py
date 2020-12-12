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
                newgrid[y][x] = "."
            else:
                nearFilled = 0
                # seat coords:
                # [-1,-1][0,-1][1,-1]
                # [-1,0 ][0,0 ][1,0 ]
                # [-1,1 ][0,1 ][1,1 ]
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == dx == 0:
                            continue
                        ynum = y
                        xnum = x
                        while True:
                            ynum += dy
                            xnum += dx
                            if(not 0 <= ynum < row) or (not 0 <= xnum < col): 
                               break
                            if data[ynum][xnum] != ".":
                                if data[ynum][xnum] == "#":
                                    nearFilled += 1
                                break

                if data[y][x] == "L" and nearFilled == 0:
                    updated = True
                    newgrid[y][x] = "#"
                elif data[y][x] == "#" and nearFilled >= 5:
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
