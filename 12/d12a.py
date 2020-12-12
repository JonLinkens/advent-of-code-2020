# File Input -----------------
datafile = open("d12.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

directions = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1,0)
}

def journey(data):
    facing = 0 # (east)

    xnum,ynum = 0, 0

    for line in data:
        cmd = line[0]
        num = int(line[1:])

        if cmd in directions:
            x,y = directions[cmd]
            xnum += x*num
            ynum += y*num
        
        elif cmd == "L":
            facing = (facing + num) % 360 #mod 360 to stay in range
        elif cmd == "R":
            facing = (facing - num) % 360
        
        else:
            if facing == 0:
                xnum += num
            elif facing == 90:
                ynum += num
            elif facing == 180:
                xnum -= num
            elif facing == 270:
                ynum -= num
    return xnum, ynum

xnum, ynum = journey(data)

print(abs(xnum)+abs(ynum))