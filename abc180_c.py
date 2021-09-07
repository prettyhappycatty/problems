#要復習

import math
N = int(input())

rev = []
for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        print(i)
        if N // i != i:
            rev.append(N // i)

for j in range(len(rev)-1,-1,-1):
    print(rev[j])
