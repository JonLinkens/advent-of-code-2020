import collections
import itertools
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
            bits = list(bin(loc)[2:].zfill(36))
            
            x_count = 0 # 2^x = amount of diff bit patterns 
            for i in range(36):
                if m[i] in ["1", "X"]:
                    bits[i] = m[i]
                    if m[i] == "X":
                        x_count += 1

            permutations = itertools.product(("1", "0"), repeat=x_count) # permutations for X values in the bit patterns
            for p in permutations:
                bitsclone = bits.copy()
                xi = 0 # x index 
                for i in range(36):
                    if bitsclone[i] == "X":
                        bitsclone[i] = p[xi] 
                        xi += 1

                val2 = int("".join(bitsclone), 2)
                mem[val2] = val
        elif line.startswith("mask"):
            m = elements[2]
    return mem

comp = compute()
#sum all keys encountered
sum_ = 0
for loc in comp:
    sum_ += comp[loc]

print(sum_)