from utils import CircularLinkedList
# File Input -----------------
datafile = open("d23.txt")
data = datafile.read()
datafile.close()
data = list(map(int, data))
# ----------------------------

def play(cups, rounds):
    chll = CircularLinkedList(cups)
    item = chll.getNode(cups[0])
    for _ in range(rounds):
        hand = [item.next.value, item.next.next.value, item.next.next.next.value]
        dest = len(cups) if item.value == 1 else item.value - 1
        while dest in hand:
            dest = len(cups) if dest == 1 else dest - 1
        while hand:
            chll.moveCups(hand.pop(), dest)
        item = item.next
    return chll.getNode(1)

def d23asol(cups):
    c = play(cups, 100)
    r, item = '', c.next
    while item != c:
        r += str(item.value)
        item = item.next
    return r

def d23bsol(cups):
    n = 10 ** 6
    n1 = 10 ** 7
    c = play(cups + list(range(10, n + 1)), n1)
    return c.next.value * c.next.next.value

print(d23asol(data))
print(d23bsol(data))