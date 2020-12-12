# File Input -----------------
datafile = open("d2.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def d2asol(data):
    count = 0
    for index, value in enumerate(data):
        line = value.split()
        rangenums = list(map(int, line[0].split("-")))
        charcount = line[2].count(line[1][0])
        if rangenums[0] <= charcount <= rangenums[1]:
            count +=1
    return count


def d2bsol(data):
    count = 0
    for index, value in enumerate(data):
        line = value.split()
        indexnums = list(map(int, line[0].split("-")))
        char_ = line[1][0]
        if line[2][(indexnums[0])-1] == char_ and line[2][(indexnums[1])-1] != char_:
            count +=1
        if line[2][(indexnums[1])-1] == char_ and line[2][(indexnums[0])-1] != char_:
            count +=1
    return count

print(d2asol(data))
print(d2bsol(data))
