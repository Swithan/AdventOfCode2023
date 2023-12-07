import re
with open("./day01.txt") as f:
  print(sum([int(v[0]+v[-1]) for v in [d for d in [re.findall(f"(\d)", l) for l in f]]]))
with open("./day01.txt") as f:
  digits = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
  print(sum([int(digits.get(v[0], v[0]) + digits.get(v[-1], v[-1])) for v in [re.findall(f"(?=(\d|{'|'.join(digits.keys())}))", l) for l in f]]))