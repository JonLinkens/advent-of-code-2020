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
    wpx, wpy = 10, 1 #waypoint coords
    xnum,ynum = 0, 0 

    for line in data:
        cmd = line[0]
        num = int(line[1:])

        if cmd in directions:
            x,y = directions[cmd]
            wpx += x*num
            wpy += y*num

        elif cmd in ["L", "R"]:
            if(cmd == "L" and num == 90) or (cmd == "R" and num == 270):
                wpx, wpy = -wpy, wpx #graph translation
            elif num == 180:
                wpx, wpy = -wpx, -wpy
            elif (cmd == "L" and num == 270) or (cmd == "R" and num == 90):
                wpx, wpy = wpy, -wpx

        else:
            xnum += wpx * num
            ynum += wpy * num

    return xnum, ynum

xnum, ynum = journey(data)
print(abs(xnum)+abs(ynum))