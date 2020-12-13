# File Input -----------------
datafile = open("d13.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

arrival = int(data[0])
busnums = data[1].split(",")
timetowait = {}

for n in busnums:
    if n == "x":
        continue
    num = int(n)
    timetowait[num] = (num * (arrival // num) + num) - arrival

earliest = min(timetowait, key=timetowait.get)
print(earliest * timetowait.get(earliest))