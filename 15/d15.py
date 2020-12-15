# File Input -----------------
datafile = open("d15.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def calcTurns(bound):
    for line in data:
        nums = list(map(int, line.strip().split(',')))
        last = {}
        lastnum = None
        for i in range(bound):
            if i < len(nums):
                n = nums[i]
            else:
                if lastnum not in last:
                    n = 0
                else:
                    n = (i-1)-last[lastnum]
            last[lastnum] = i-1
            lastnum = n
        return n

print(calcTurns(2020)) 
print(calcTurns(30000000)) # takes a while but for this use case its fine

