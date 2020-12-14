import collections
# File Input -----------------
datafile = open("d14.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

m = []
def compute():
    mem = collections.defaultdict(int)

    for line in data:
        elements = line.split(" ")
        if line.startswith("mem"):
            # splitting data
            loc = int(elements[0][elements[0].index("[") + 1:elements[0].index("]")]) #everything between []
            val = int(elements[2])
            bits = list(bin(val)[2:].zfill(36))

            for i in range(36):
                if m[i] in ["0", "1"]:
                    bits[i] = m[i]
            val2 = int("".join(bits), 2)
            mem[loc] = val2
    
        elif line.startswith("mask"):
            m = elements[2]
    return mem

comp = compute()
#sum all keys encountered
sum_ = 0
for loc in comp:
    sum_ += comp[loc]

print(sum_)
