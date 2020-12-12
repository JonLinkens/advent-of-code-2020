# File Input -----------------
datafile = open("d9.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
data = list(map(int, data))
# ----------------------------

def d9asol(data):
    nrange = 25
    for i in range(nrange, len(data)):
        val = data[i]
        isTotal = False

        for j in range(i - nrange, i):
            for k in range(j, i):
                if data[j] + data[k] == val:
                    isTotal = True
            
            if isTotal:
                break
        if not isTotal:
            return val

def d9bsol(data, parta):
    # precomputation:
    nums = [0]
    for linenum in data:
        nums.append(nums[-1]+linenum)
    
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            numsum = nums[j + 1]-nums[i]
            if numsum == parta:
                lo = min(data[i:j+1])
                hi = max(data[i:j+1])
                return lo+hi

parta = d9asol(data); print(parta)
print(d9bsol(data,parta))
