# File Input -----------------
datafile = open("d6.txt")
data1 = datafile.read()
data = data1.split("\n\n")
datafile.close()
# ----------------------------

# using sets to avoid duplicates
def d6asol(data):
    groups = []
    for line in data:
        groups.append(set(line.replace("\n","")))
    sums = 0
    for elements in groups:
        sums += len(elements)
    return sums

def d6bsol(data):
    count = 0
    for line in data:
        ans = line.split("\n")
        initial = set(ans[0])

        for a in ans[1:]:
            initial = initial.intersection(a)
        count += len(initial)
    return count

print(d6asol(data))
print(d6bsol(data))