import sys
sys.setrecursionlimit(400000000)

N = int(input())

g = {}
col = [-1]
for i in range(N-1):
    tmpA, tmpB = map(int, input().split())
    if tmpA-1 not in g.keys():
        g[tmpA-1] = []
    if tmpB-1 not in g.keys():
        g[tmpB-1] = []
    g[tmpA-1].append(tmpB-1)
    g[tmpB-1].append(tmpA-1)
    col.append(-1)

if N == 2:
    print(tmpA)
    exit()

#print(g)
colcnt = [0,0]

def dfs(pos, cr):
    col[pos] = cr
    colcnt[cr] += 1
    #print(colcnt[0],colcnt[1], N//2)
    for i in g[pos]:
        if(col[i] == -1):
            dfs(i, 1-cr)

a = dfs(0,0)
#print(a, col)

if colcnt[0] >= colcnt[1]:
    idx = 0
else:
    idx = 1

ret = []
cnt = 0
for i in range(N):
    if col[i] == idx:
        ret.append(str(i+1))
        cnt += 1
    if cnt >= N//2:
        break

#print(ret)
L=' '.join(ret)
print(L)
