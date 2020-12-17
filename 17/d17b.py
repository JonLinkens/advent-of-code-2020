# rank 325!
# minimal changes, just adding an extra dimension (w)
import collections
# File Input -----------------
datafile = open("d17.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

grid = {}
for y, line in enumerate(data):
    for x, character in enumerate(line):
        if character == '#':
            grid[(0, 0, y, x)] = character # storing each # in grid as tuple of coords

for _ in range(6): # 6 cycles
    active = collections.Counter() # counter dict

    for (w,z,y,x), _ in grid.items(): # for loops for possible dimension coords
        for wnum in (-1, 0, 1):
            for znum in (-1, 0 , 1):
                for ynum in (-1, 0 , 1):
                    for xnum in (-1, 0, 1):
                        if wnum == znum == ynum == xnum == 0:
                            continue
                        active[(w+wnum, z+znum, y+ynum, x+xnum)] +=1


    newgrid = {}
    for k, v in active.items():
        if v == 3: # if 3 neighbouring cubes are active
            newgrid[k] = '#'

    for k in grid:
        if active[k] in {2, 3}:  # if exactly 2 or 3 neighbour cubes are active
            newgrid[k] = '#'
    grid = newgrid

print(len(grid))