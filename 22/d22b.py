# some refactors from part a 
from collections import deque
# File Input -----------------
datafile = open("d22.txt")
data1 = datafile.read()
data = data1.split("\n\n")
datafile.close()
# ----------------------------

# Helper Functions -----------
def populateDeck(pnum):
    cards = data[pnum][data[pnum].index(":")+2:].split("\n")
    cards = list(map(int, cards))
    return deque(cards)

def deckScore(d):
    s = 0
    for i in range(len(d)):
        s += d[i] * (len(d)-i)
    return s
# ----------------------------
def game():
    p = [populateDeck(0), populateDeck(1)]
    _, deck = play(p[0],p[1])
    return deckScore(deck)

def play(p1,p2):
    pastcards = set()
    while len(p1) > 0 and len(p2) > 0:
        if (tuple(p1), tuple(p2)) in pastcards:
            return 1, None
        pastcards.add((tuple(p1), tuple(p2)))

        p1_card = p1.popleft()
        p2_card = p2.popleft()
        #print(str(p1_card)+" "+str(p2_card))
        if p1_card <= len(p1) and p2_card <= len(p2):
            p1copy = deque(list(p1)[:p1_card])
            p2copy = deque(list(p2)[:p2_card])
            subresult = play(p1copy, p2copy)
            w, _ = subresult
        else:
            w = 1 if p1_card > p2_card else 2
        if w == 1:
            #print("p1")
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            #print("p2")
            p2.append(p2_card)
            p2.append(p1_card)
    if len(p1) == 0:
        return 2, p2
    else:
        return 1, p1

print(game())