import re
import time
start_time = time.time()
file = open('day06.txt')
file = [l for l in file]
times = file[0]
times = re.findall(r'\d+', times)

distances = file[1]
distances = re.findall(r'\d+', distances)

print(times)
print(distances)

total = 1

for race in range(len(times)):
    total_time = int(times[race])
    min_distance = int(distances[race])

    wait = 1
    left_time = total_time-wait
    speed = 1
    travelled = left_time

    ways = 0

    # for each possible wait time
    for i in range(1, int(total_time)):
        wait = i
        speed = wait
        left_time = total_time-wait

        travelled = left_time*speed
        if travelled > min_distance:
            ways += 1
    total *= ways
print("--- %s seconds ---" % (time.time() - start_time))

print(total)