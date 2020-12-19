import re
from functools import lru_cache
# File Input -----------------
datafile = open("d19.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

rules, regex = {}, {}
# populate rules dict
line = 0
while data[line] != "":
    num = int(data[line][:data[line].index(":")])
    rule = data[line][data[line].index(":") + 2:]
    rules[num] = rule
    line+=1

@lru_cache(None)
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
    if num in regex:
        return regex[num]

    num1 = regexConvert(rules[num])
    regex[num] = num1
    return num1

c = 0
line += 1
zeroth = getRe(0)

while line < len(data):
    valid = bool(re.fullmatch(zeroth, data[line]))
    c += valid
    line +=1

print(c)