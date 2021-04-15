import math

N = int(input())

min_dist = 10**13
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        dist = i + N // i - 2
        if min_dist > dist:
            min_dist = dist
print(dist)