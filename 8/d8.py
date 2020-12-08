# File Input -----------------
datafile = open("d8.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def d8asol(data):
    visited = {}
    linenum = 0
    accval = 0

    while linenum not in visited and linenum < len(data):
        line = data[linenum]
        visited[linenum] = line
        cmd, num = line.split(" ")
        if cmd == "acc":
            accval += int(num)
            linenum +=1
        elif cmd == "jmp":
            linenum += int(num)
        elif cmd == "nop":
            linenum += 1
    return accval

def d8bsol(data):
    # brute force
    for i in range(len(data)):
        if data[i].startswith("acc"):
            continue
        if data[i].startswith("nop"):
            clone = data.copy()
            clone[i] = "jmp" + clone[i][3:]
        else:
            clone = data.copy()
            clone[i] = "nop" + clone[i][3:]
        
        run = bHelper(clone) #testing each possibility
        if run:
            return run
    return None

def bHelper(data):
    linenum = 0
    accval = 0

    def bHelper(line):
        cmd, num = line.split(" ")
        if cmd == "acc":
            return int(num), 1
        elif cmd == "jmp":
            return 0, int(num)
        else:
            return 0, 1
    visited = {}
    linenum = 0
    accval = 0
    while linenum not in visited and linenum < len(data):
        line = data[linenum]
        visited[linenum] = line
        acc, jmp = bHelper(line)
        accval += acc
        linenum += jmp

    if linenum >= len(data):
        return accval

    return None# infinite check

print(d8asol(data))
print(d8bsol(data))