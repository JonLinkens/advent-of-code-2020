import re
with open("d4.txt","r") as file:
    data = file.read().replace("\n"," ").split("  ")

def d4asol (passports):
    validpassports = 0
    for element in passports:
        counter = 0
        # regex search to see if contained in each passport
        if re.search(r"byr:",element):
            counter += 1
        if re.search(r"iyr:",element):
            counter += 1
        if re.search(r"eyr:",element):
            counter += 1
        if re.search(r"hgt:",element):
            counter += 1
        if re.search(r"hcl:",element):
            counter += 1
        if re.search(r"ecl:", element):
            counter += 1
        if re.search(r"pid:", element):
            counter += 1
        # if all regex passed (7) increment count
        if counter == 7:
            validpassports += 1 
    return validpassports

def d4bsol (passports):
    validpassports = 0
    for element in passports:
        counter = 0
        # 1920 < byr < 2002
        if 	re.search(r"byr:(19[2-9][0-9]|200[0-2])\b", element):
            counter += 1
        # 2010 < iyr < 2020
        if  re.search(r"iyr:(201[0-9]|20[0-2]0)\b", element):
            counter += 1
        # 2020 < eyr < 2030
        if  re.search(r"eyr:(202[0-9]|2030)\b", element):
            counter += 1
        # 150 < hgt(cm) < 193 || 59 < hgt(in) < 76
        if  re.search(r"(hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in|hgt:1[5-8][0-9]cm|hgt:19[0-3]cm)\b", element):
            counter += 1
        # hcl[0] == "#" and len(hcl) == 6 and contains only 0-9, a-f
        if  re.search(r"hcl:#([0-9]|[a-f]){6}\b", element):
            counter += 1	
        # ecl is exactly one of the colour selections
        if  re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b", element):
            counter += 1
        # lenpid == 9 
        if  re.search(r"pid:([0-9]){9}\b", element):
            counter += 1
        # if all regex passed (7) increment count
        if counter == 7:
            validpassports += 1
    return validpassports


print(d4asol(data))
print(d4bsol(data))