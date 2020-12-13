from sympy.ntheory.modular import crt # chinese remainder theorem library to avoid lengthy implementation
# File Input -----------------
datafile = open("d13.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

busnums = data[1].split(",")
mod, rem = [], []

for index, value in enumerate(busnums):
    if value != "x":
        mod.append(int(value))
        rem.append((-index) %  mod[-1])

print(crt(mod, rem)) # feels cheap but it works 