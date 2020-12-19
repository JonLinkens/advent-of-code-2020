import re
# File Input -----------------
datafile = open("d19.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

rules = {}
# populate rules dict
line = 0
while data[line] != "":
    num = int(data[line][:data[line].index(":")])
    rule = data[line][data[line].index(":") + 2:]
    rules[num] = rule
    line+=1

def regexConvert(r):

    if "|" in r:# based off assumption only rule has only left/right side
        left = [int(i) for i in r[:r.index("|") - 1].split(" ")]
        right = [int(i) for i in r[r.index("|") + 2:].split(" ")]

        leftre = "(" + ")(".join([getRe(i) for i in left]) + ")"
        rightre = "(" + ")(".join([getRe(i) for i in right]) + ")"
        rule = f"({leftre})|({rightre})"# fstring to construct rule

    elif '"' in r:
        rule = r[1]
    else:
        elements = [int(i) for i in r.split(" ")]
        rule = "("+")(".join([getRe(i) for i in elements]) + ")"
    return rule

def getRe(num):
    if num == 11:
        return rule11
    if num == 8:
        return rule8
    
    num1 = regexConvert(rules[num])
    return num1


rule42 = getRe(42)
rule31 = getRe(31)

rule8 = f"({rule42})+" # match rule 42 1-n times

ruleset11 = []
for i in range(1, 20):
    ruleset11.append((f"({rule42}){{{i}}}({rule31}){{{i}}}")) # 42 11 31
rule11 = "(" + ")|(".join([i for i in ruleset11]) + ")"

c = 0
line += 1
zeroth = getRe(0)

while line < len(data):
    valid = bool(re.fullmatch(zeroth, data[line]))
    c += valid
    line +=1

print(c)