def d3sol(data,xnum):
    index = 0
    treecount = 0
    for line in data:
        if line[index % 31] == "#":
            treecount += 1
        index +=xnum
    return treecount

xnum = int(input("Enter x val: "))
ynum = int(input("Enter y val: "))


# File Input -----------------
datafile = open("d3.txt")
data1 = datafile.read()
data = data1.splitlines()[::ynum]
datafile.close()
# ----------------------------

print(d3sol(data, xnum))