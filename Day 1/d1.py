# File Input -----------------
datafile = open("d1.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
data = list(map(int, data))
# ----------------------------

def day1a(data, target):
    nums = {}
    for index, value in enumerate(data):
        d = target - value
        if(d in nums):
            return d*value
        nums[value] = index
    return nums

def day1b(data, target):
     for i, a in enumerate(data):
         for j, b in enumerate(data[i+1:-1]):
             for c in data[j+1:]:
                 if(a+b+c) == target:
                     return a*b*c


print(day1a(data, 2020))
print(day1b(data, 2020))




