import collections
# File Input -----------------
datafile = open("d20.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

# Helper functions -----------
def rotate_tile(t, n): 
    return t[n:] + t[:n]

def new_coords(d):
    if d == 0:
        return 0, 1
    if d == 1:
        return 1, 0
    if d == 2:
        return 0, -1
    if d == 3:
        return -1, 0
# ----------------------------

tiles = {}
ln = 0
# populating dict with tile ids
tile = []
while ln < len(data):
    tile = []
    tileid = int(data[ln][data[ln].index(" ") + 1:-1]) # parsing tile id
    for i in range(10):
        ln += 1
        tile.append(data[ln])
    tiles[tileid] = tile
    ln+=2 

# getting edges of each tile
edges = {}
for tileid in tiles:
    tile = tiles[tileid]
    edge0 = tile[0]
    edge1 = "".join([y[-1] for y in tile])
    edge2 = tile[-1][::-1]
    edge3 = "".join([y[0] for y in tile][::-1])
    edges[tileid] = [edge0, edge1, edge2, edge3]

# constructing grid
grid = collections.defaultdict(lambda: None) # None value for nonexistent key
first_tile = list(tiles.keys())[0]

stack = [(first_tile, (0,0))]
grid[(0,0)] = first_tile
visited = {first_tile}

while len(stack) > 0:
    tileid, coords = stack.pop()

    for d in range(4): # 4 directions
        edge = edges[tileid][d]

        identified = False
        for etc in edges:
            if etc in visited:
                continue

            if edge in edges[etc] or edge[::-1] in edges[etc]: #edge or reversed variant
                if edge in edges[etc]:
                    edges[etc] = [e[::-1] for e in edges[etc][::-1]]
                
                elif edge[::-1] in edges[etc]:
                    pass

                opp_side = edges[etc].index(edge[::-1])
                identified = True
                edges[etc] = rotate_tile(edges[etc], (opp_side - (d + 2) % 4) % 4) # 4 direction check
                assert edges[etc][(d + 2) % 4] == edge[::-1]

                new_c = new_coords(d)
                newcoords = coords[0] + new_c[0], coords[1] + new_c[1]

                if newcoords in grid:
                    break
                grid[newcoords] = etc
                stack.append((etc, newcoords))
                visited.add(etc)
            if identified:
                break

for coords in grid:
    pass

for tileid in tiles:
    identified = False
    for coords in grid:
        if tileid == grid[coords]:
            identified = True
            break
    if not identified:
        print(tileid)

min_x, min_y, max_x, max_y = 100000, 100000, -100000, -100000

for x,y in grid:
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

mult = 1
for x in min_x, max_x:
    for y in min_y, max_y:
        tileid = grid[(x,y)]
        mult *= tileid

print(mult)

