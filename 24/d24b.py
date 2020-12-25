# File Input -----------------
datafile = open("d24.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

# Helper ---------------------
def adjacent(coords): # returns hexagons surrounding coords
    adj = []
    for d in directions:
        changes = directions[d]
        adjcoords = (coords[0] + changes[0], coords[1] + changes[1])
        adj.append(adjcoords)
    return adj

def adjacent_count(coords):
    c = 0
    for adj in adjacent(coords):
        if adj in flipped:
            c +=1
    return c

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

def step():
    stack = set()
    history = set()
    new_flipped = flipped.copy()

    for h in flipped:
        stack.add(h)
        stack.update(adjacent(h))

    while len(stack) > 0:
        coords = stack.pop()
        if coords in history:
            continue
    
        history.add(coords)
        
        adj_count = adjacent_count(coords)
        if coords in flipped and (adj_count == 0 or adj_count > 2):
            new_flipped.remove(coords)

        elif coords not in flipped and (adj_count == 2):
            new_flipped.add(coords)

    return new_flipped

flipped = set() # hexagons flipped to black
for line in data:
    coords = Coordinates(line)
    if coords in flipped:
        flipped.remove(coords)
    else:
        flipped.add(coords)

for _ in range(100):
    flipped = step()

print(len(flipped))