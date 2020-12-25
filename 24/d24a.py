# File Input -----------------
datafile = open("d24.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

# https://www.redblobgames.com/grids/hexagons/
directions = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (1, -1),
    "nw": (0, -1),
    "se": (0, 1),
    "sw": (-1, 1)
}


def Coordinates(l):
    i = 0
    x,y = 0,0
    while i < len(l):
        if i < len(l) - 1 and l[i:i+2] in directions: # 2 letter dir check
            dirs = l[i:i+2]
            i +=2
        elif l[i] in directions:
            dirs = l[i]
            i += 1
         
        changes = directions[dirs]
        x += changes[0]
        y += changes[1]
    return x,y

flipped = set() # hexagons flipped to black
for line in data:
    coords = Coordinates(line)
    if coords in flipped:
        flipped.remove(coords)
    else:
        flipped.add(coords)

print(len(flipped))