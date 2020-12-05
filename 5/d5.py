# File Input -----------------
datafile = open("d5.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

# 128 rows
# F = lower half
# B = upper half
# can be considered as binary where F = 0 and B = 1
# 8 columns
# L = lower half 
# R = upper half
# so L = 0 and R = 1
# so just replace with 0s and 1s
# then convert from binary to int - int(x, 2)

def d5asol(data):
    max_ = 0
    for index, _ in enumerate(data):
        row = int(data[index][:7].replace("F", "0").replace("B","1"), 2)
        col = int(data[index][7:].replace("L", "0").replace("R","1"), 2)
        data[index] = 8 * row + col
        max_ = max(data[index], max_)
    return max_

# Numbers are sequential so can take difference in sum of data range and actual data set
def d5bsol(data):
    return(sum(range(min(data),max(data)+1))-sum(data))


print(d5asol(data))
print(d5bsol(data))
