# File Input -----------------
datafile = open("d7.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

graph1 = {}
graph2 = {}
def aformatColour(line):
    # formatting data for later use
    line = line.split(" ")
    colour = " ".join(line[:line.index("contain") - 1]) # after keyword contain is a list of the children
    childNode = " ".join(line[line.index("contain") + 1:]).split(", ") # children are separated by a comma and then a space

    for element in childNode:
        if element == "no other bags.": # an empty bag
            continue
        split = element.split(" ") 
        bagcolour = " ".join(split[1:-1])
        if bagcolour not in graph1:
            graph1[bagcolour] = set() # adding bags to graph as sets
        graph1[bagcolour].add(colour) # adding parent bag



def d7asol(data):
    for line in data:
        aformatColour(line)
    num = []
    term = ["shiny gold"]
    encountered = set()
    # start with shiny gold bag and perform bottom up DFS on graph 
    while len(term) > 0:
        pop = term.pop()
        if pop in encountered: # keep track of bags already encountered
            continue
        encountered.add(pop)
        if pop in graph1: # if bag is in the graph then check all its parents
            pNode = graph1[pop]
            for n in pNode:
                term.append(n)
        else:
            num.append(pop)
    return (len(encountered)-1)



def bFormatColour(line):
    # formatting data for later use
    line = line.split(" ")
    colour = " ".join(line[:line.index("contain") - 1]) # after keyword contain is a list of the children
    if colour not in graph2:
        graph2[colour] = set()

    childNode = " ".join(line[line.index("contain") + 1:]).split(", ") # children are separated by a comma and then a space
    for element in childNode:
        if element == "no other bags.": # an empty bag
            continue

        split = element.split(" ") 
        bagamt = int(split[0]) # each element starts with a number (of bags)
        bagcolour = " ".join(split[1:-1])
        graph2[colour].add((bagamt, bagcolour)) #keeping track of child bag, given parent bag



def d7bsol(data):
    # part a but tracking total children of bag instead of parents. must track quantity in search
    for line in data:
        bFormatColour(line)
    amt = 0 # amount to keep track of
    term = [(1, "shiny gold")]

    # DFS
    while len(term) > 0:
        num, clr = term.pop()
        amt+=num # bags popped added to total amount

        if clr in graph2:
            cNode = graph2[clr]
            for i, node in cNode:
                term.append((i * num, node)) # for every child bag, amount = amount of parent bag * how many children bags inside
    
    return(amt-1) 

print(d7asol(data))
print(d7bsol(data))
