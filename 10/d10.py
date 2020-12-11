from functools import lru_cache
# File Input -----------------
datafile = open("d10.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
data = list(map(int, data))
data += [0]
data.sort()
# ----------------------------

def d10asol():
    def joltagediff():
        threediff = 0
        onediff = 0
        for i in range(len(data)-1):
            diff = data[i+1]-data[i]
            if diff == 3:
                threediff +=1
            elif diff == 1:
                onediff += 1
        return threediff+1, onediff+1

    one, three = joltagediff()
    return one * three

@lru_cache(None) # easy memoisation
def d10bsol(i):
    # base case
    if i == len(data) - 1:
        return 1

    t = 0
    nexti = i+1
    while nexti < len(data) and data[nexti] - data[i] <= 3:
        t += d10bsol(nexti)
        nexti += 1
    return t

print(d10asol())
partb = d10bsol(0); print(partb)