import re
import time
from collections import Counter

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

custom_order = 'AKQT98765432J'

def custom_sort_key(s):
    return [custom_order.index(char) for char in s]

def sort_and_count_occurrences(input_string, custom_order):
    # Sort the string based on the custom order
    sorted_string = ''.join(sorted(input_string, key=lambda x: custom_order.index(x)))

    # Count occurrences of each character
    char_occurrences = Counter(sorted_string)

    # Create the final sorted string
    final_sorted_string = ''.join([char * char_occurrences[char] for char in custom_order if char_occurrences[char] > 0])

    return final_sorted_string, char_occurrences

for hand in h.keys():
    hand2 = hand

    if 'J' in hand:
        if hand == 'JJJJJ':
            hand = "AAAAA"
        hnd = hand.replace("J", "")
        sorted_string, counter = sort_and_count_occurrences(hnd, custom_order)
        if all(count == 1 for count in counter.values()):
            hand.replace("J", "A")
        else:
            hand = hand.replace("J", counter.most_common(1)[0][0])
    # 5 cards
    a = re.findall(hand[0], hand)
    if len(a) == 5:
        addHand(five, hand2)
    elif len(a) == 4:
        addHand(four, hand2)
    elif len(a) == 3:
        c = hand.replace(a[0], "")
        if len(re.findall(c[0], c)) == 2:
            addHand(full, hand2)
        else: 
            addHand(three, hand2)


    elif len(a) == 2:
        c = hand.replace(hand[0], "")
        # 3 cards left
        if len(re.findall(c[0], c)) == 3:
            addHand(full, hand2)
        elif len(re.findall(c[0], c)) == 2:
            addHand(double, hand2)
        else:
            #2 cards left
            c = c.replace(c[0], "")
            if len(re.findall(c[0], c)) == 2:
                addHand(double, hand2)
            else:
                addHand(pair, hand2)
    else:
        c = hand.replace(a[0], "")
        # 4 cards left
        if len(re.findall(c[0], c)) == 4:
            addHand(four, hand2)
        elif len(re.findall(c[0], c)) == 3:
            addHand(three, hand2)
        elif len(re.findall(c[0], c)) == 2:
            c = c.replace(c[0], "")
            # 2 cards left
            if len(re.findall(c[0], c)) == 2:
                addHand(double, hand2)
            else:
                addHand(pair, hand2)
        else: 
            c = c.replace(c[0], "")
            # 3 cards left
            if len(re.findall(c[0], c)) == 3:
                addHand(three, hand2)
            elif len(re.findall(c[0], c)) == 2:
                addHand(pair, hand2)
            else:
                #2 cards left
                c = c.replace(c[0], "")
                if len(re.findall(c[0], c)) == 2:
                    addHand(pair, hand2)
                else:
                    addHand(height, hand2)


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


"""
SOLUTIONS : 

def eval(line):
    hand, bid = line.split()
    hand = hand.translate(str.maketrans('TJQKA', face))
    best = max(type(hand.replace('0', r)) for r in hand)
    return best, hand, int(bid)

def type(hand):
    return sorted(map(hand.count, hand), reverse=True)

for face in 'ABCDE', 'A0CDE':
    print(sum(rank * bid for rank, (*_, bid) in
        enumerate(sorted(map(eval, open('data.txt'))), start=1)))
        """