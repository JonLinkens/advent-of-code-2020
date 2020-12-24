from collections import deque
# File Input -----------------
datafile = open("d22.txt")
data1 = datafile.read()
data = data1.split("\n\n")
datafile.close()
# ----------------------------

# queue for each player
# while len of queues > 0 
# pop both
# push to winner (their card first)
# iterate backwards and sum

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
    result = play(p[0],p[1])
    if result == 1:
        r = deckScore(p[0])
    else:
        r = deckScore(p[1])
    return r

def play(p1,p2):
    while len(p1) > 0 and len(p2) > 0:
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        #print(str(p1_card)+" "+str(p2_card))
        if p1_card > p2_card:
            #print("p1")
            p1.append(p1_card)
            p1.append(p2_card)
        elif p2_card > p1_card:
            #print("p2")
            p2.append(p2_card)
            p2.append(p1_card)
    if len(p1) == 0:
        return 2
    elif len(p2) == 0:
        return 1

print(game())