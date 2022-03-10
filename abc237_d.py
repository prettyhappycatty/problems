N = int(input())
S = input()

from collections import deque

d = deque([N])

for i in range(N-1,-1,-1):
    #print(S[i])
    if S[i] == "R":
        d.appendleft(i)
    else:
        d.append(i)

l = []
for i in range(N+1):
    l.append(d.popleft())
print(*l)
