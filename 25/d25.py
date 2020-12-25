# clean code for once 
# File Input -----------------
datafile = open("d25.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
data = list(map(int, data))
# ----------------------------

card_key, door_key = data[0], data[1]
val, key, subnum, div  = 1, 1, 7, 20201227

while val != card_key:
    val = (val * subnum) % div
    key = (key * door_key) % div
print(key)