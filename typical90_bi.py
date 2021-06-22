from collections import deque


d = deque()

N = int(input())


for i in range(N):
    tmp1, tmp2 = map(int, input().split())
    if tmp1 == 1:
        d.appendleft(tmp2)
    elif tmp1 == 2:
        d.append(tmp2)
    elif tmp1 == 3:
        print(d[tmp2-1])
