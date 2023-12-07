import re 
file = list(open("day04.txt"))

result = 0
more = [1 for i in range(len(file))]
for l, line in enumerate(file):
    line = line.split(': ')[1]
    wins = line.split(" |")[0]
    wins = re.findall(r'\d+', wins)
    numbers = line.split("| ")[1]
    numbers = re.findall(r'\d+', numbers)

    total = 0
    copy = 0

    for same in set(wins) & set(numbers):
        copy += 1
        total = 1 if total == 0 else total*2

    for i in range(copy):
        more[l+i+1] += more[l]
    result += total

print(result)
cards = sum(more)
print(cards)