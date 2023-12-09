import re
import time
start_time = time.time()
file = open("day07.txt")
h = {}
for l in file:
    hand = l.split("\n")[0].split(' ')
    h[hand[0]] = int(hand[1])

five = []
four = []
full = []
three = []
double = []
pair = []
height = []

def addHand(place, hand):
    place.append(hand)

for hand in h.keys():

    # 5 cards
    a = re.findall(hand[0], hand)
    if len(a) == 5:
        addHand(five, hand)
    elif len(a) == 4:
        addHand(four, hand)
    elif len(a) == 3:
        c = hand.replace(a[0], "")
        if len(re.findall(c[0], c)) == 2:
            addHand(full, hand)
        else: 
            addHand(three, hand)


    elif len(a) == 2:
        c = hand.replace(hand[0], "")
        # 3 cards left
        if len(re.findall(c[0], c)) == 3:
            addHand(full, hand)
        elif len(re.findall(c[0], c)) == 2:
            addHand(double, hand)
        else:
            #2 cards left
            c = c.replace(c[0], "")
            if len(re.findall(c[0], c)) == 2:
                addHand(double, hand)
            else:
                addHand(pair, hand)
    else:
        c = hand.replace(a[0], "")
        # 4 cards left
        if len(re.findall(c[0], c)) == 4:
            addHand(four, hand)
        elif len(re.findall(c[0], c)) == 3:
            addHand(three, hand)
        elif len(re.findall(c[0], c)) == 2:
            c = c.replace(c[0], "")
            # 2 cards left
            if len(re.findall(c[0], c)) == 2:
                addHand(double, hand)
            else:
                addHand(pair, hand)
        else: 
            c = c.replace(c[0], "")
            # 3 cards left
            if len(re.findall(c[0], c)) == 3:
                addHand(three, hand)
            elif len(re.findall(c[0], c)) == 2:
                addHand(pair, hand)
            else:
                #2 cards left
                c = c.replace(c[0], "")
                if len(re.findall(c[0], c)) == 2:
                    addHand(pair, hand)
                else:
                    addHand(height, hand)

custom_order = 'AKQJT98765432'

def custom_sort_key(s):
    return [custom_order.index(char) for char in s]

five = sorted(five, key=custom_sort_key, reverse=True)
four = sorted(four, key=custom_sort_key, reverse=True)
full = sorted(full, key=custom_sort_key, reverse=True)
three = sorted(three, key=custom_sort_key, reverse=True)
double = sorted(double, key=custom_sort_key, reverse=True)
pair = sorted(pair, key=custom_sort_key, reverse=True)
height = sorted(height, key=custom_sort_key, reverse=True)

rank = 1
total = 0

for i in height+pair+double+three+full+four+five :
    total += h[i]*rank
    rank += 1

print(total)
print("--- %s seconds ---" % (time.time() - start_time))
