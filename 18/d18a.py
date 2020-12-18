# Rank 835 (code refactor)
# File Input -----------------
datafile = open("d18.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

def calc(exp):
    op = ""
    val = 0
    prev_val = ""

    index = 0
    while index < len(exp):
        c = exp[index]
        if c.isdigit():
            prev_val += c
        
        elif c in ["+", "*"]:
            if op != "":
                if op == "+":
                    val += int(prev_val)
                else:
                    val *= int(prev_val)
            else: # setting initial value
                val = int(prev_val)
        
            prev_val = ""
            op = c
        elif c == "(": # parentheses balance check
            left = 1
            right = 0
            start = index + 1

            while left != right and index < len(exp):
                index +=1
                left += exp[index] == "("
                right += exp[index] == ")"

            prev_val = calc(exp[start:index])
        index +=1

    if op != "": # final op
        if op == "+":
            val += int(prev_val)
        else:
            val *= int(prev_val)
    return val 

sum_ = 0
for element in data:
    element = element.replace(" ", "")
    sum_ += calc(element)

print(sum_)
