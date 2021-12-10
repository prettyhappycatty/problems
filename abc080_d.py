from typing import AnyStr


N, C = map(int, input().split())

L = 10**5 + 1
#L = 20
time = [0 for _ in range(L)]#0-index

CC=[]
for i in range(C):
    CC.append([0 for _ in range(L)])

for i in range(N):
    s, t, c= map(int, input().split())
    CC[c-1][s-1] += 1
    CC[c-1][t] -=1

#print(CC)


ans=[]
for i in range(C):
    ans.append([0 for _ in range(L)])

for i in range(len(CC)):
    s = 0
    for j in range(L):
        s += CC[i][j]
        if s > 0:
            ans[i][j] = 1
#print(CC)

ans2 = [0 for _ in range(L)]#0-index

for j in range(L):
    cs = 0
    for i in range(len(CC)):
        cs += ans[i][j]
    ans2.append(cs)

print(max(ans2))
