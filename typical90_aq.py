import sys
sys.setrecursionlimit(100000000)
from collections import deque

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rg, cg = map(int, input().split())

S = []

neighbor = [(0,1),(1,0),(0,-1),(-1,0)]

F = [[[10**9 for _ in range(4)] for _ in range(W)] for _ in range(H)]
flg = [[-1 for _ in range(W)] for _ in range(H)]


for i in range(H):
    tmp = input()
    S.append(tmp)

#print(S)
for i in range(4):
    F[rs-1][cs-1][i] = 0


Q = deque()
for i in range(4):
    Q.append((rs-1, cs-1, i))

while Q:
#    print(current[0],current[1])
    current = Q.popleft()
    i = current[2]
    nei = neighbor[i]
    x = current[0] + nei[0]
    y = current[1] + nei[1]
    if x < 0 or y < 0 or x > H-1 or y > W-1 or S[x][y] == "#":
#            print("con")
        continue

#        print(x,y,i,F[x][y][i],">?",F[current[0]][current[1]][i],nei[0] == vec[0] and nei[1] == vec[1])
    for j in range(len(neighbor)):
        if i == j and  F[x][y][i] > F[current[0]][current[1]][i]:#方向が変わらない
            F[x][y][j] = F[current[0]][current[1]][i]
            flg[x][y] = 1
            Q.append((x,y,i))
        elif i != j and F[x][y][j] > F[current[0]][current[1]][i]+1: #方向が変わるけど最小値の場合
            F[x][y][j] = F[current[0]][current[1]][i]+1
            flg[x][y] = 1
            Q.append((x,y,i))
        

#print(F)
print(min(F[rg-1][cg-1][0], F[rg-1][cg-1][1],F[rg-1][cg-1][2],F[rg-1][cg-1][3]))

