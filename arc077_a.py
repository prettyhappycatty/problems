import collections
from collections import deque

n = int(input())
a = list(map(int, input().split()))

b = deque()

flg = 0 #昇順か降順かを管理

def turn(i, flg):
    if flg == 0:
        b.append(a[i])
    else:
        b.appendleft(a[i])

    return 1 - flg

f = 0
for i in range(n):
    f = turn(i, f)

if f == 0:
    print(*b)
else:
    b.reverse()
    print(*b)