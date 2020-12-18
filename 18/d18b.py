# Rank 313 (code refactor)
# File Input -----------------
datafile = open("d18.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def calc(exp):
    mults = []
    prev_val = ""
    i = 0
    isLastAdd = False

    while i < len(exp):
        c = exp[i]
        if c.isdigit():
            prev_val += c
        
        elif c == "+":
            sums = [int(prev_val)] # nums to sum
            prev_val = ""
            i += 1

            while i < len(exp):
                c = exp[i]

                if c.isdigit():
                    prev_val += c 
                elif c == "(":
                    left = 1
                    right = 0
                    start = i +1
                    
                    while left != right and i < len(exp):
                        i += 1
                        left += exp[i] == "("
                        right += exp[i] == ")"
                    prev_val = calc(exp[start:i])

                elif c == "*":
                    break
                
                elif c == "+":
                    sums.append(int(prev_val))
                    prev_val = ""
                i += 1
    
            if i == len(exp):
                isLastAdd = True
            if prev_val != "":
                sums.append(int(prev_val))
            mults.append(sum(sums))
            prev_val = ""

        elif c == "*":
            mults.append(int(prev_val))
            prev_val = ""

        elif c == "(":
            left = 1
            right = 0
            start = i + 1

            while left != right and i < len(exp):
                i += 1
                left += exp[i] == "("
                right += exp[i] == ")"
            prev_val = calc(exp[start:i])
        i += 1

    if prev_val != "" and not isLastAdd:
        mults.append(int(prev_val))

    total = 1
    for j in mults:
        total *= j
    return total 

sum_ = 0
for element in data:
    element = element.replace(" ", "")
    sum_ += calc(element)

print(sum_)
