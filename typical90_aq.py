H, W = map(int, input().split())
rs, cs = map(int, input().split())
rg, cg = map(int, input().split())

# 0-indexに変更
rs -= 1
cs -= 1
rg -= 1
cg -= 1

S = []
for i in range(H):
    tmpS = input()
    S.append(tmpS)

#print(S)

from collections import deque

def bfs(now, g, h, w, S):
    neigh = [[0,1],[0,-1],[1,0],[-1,0]]
    C = [[[10**9 for _ in range(4)] for _ in range(w)] for _ in range(h)]#距離の初期化
    queue = deque([now])
    for j in range(4):
        C[now[0]][now[1]][j] = 0 # 自分との距離は0 start地点のマトリックスは全方向１

    while queue:
        #rint(queue)
        v = queue.popleft()
        #print(v)
        for i in range(len(neigh)):#g[v]:
            x = v[0]+neigh[i][0]
            y = v[1]+neigh[i][1]
            if 0<= x < h and 0<= y < w and S[x][y] != "#":
                chg_flg = False
                for j in range(4):
                    if i == j and C[x][y][j] > C[v[0]][v[1]][i]: #方向転換しないとき
                        C[x][y][j] = C[v[0]][v[1]][i]
                        chg_flg = True
                    elif C[x][y][j] > C[v[0]][v[1]][i]+1: #方向転換する
                        C[x][y][j] = C[v[0]][v[1]][i]+1
                        chg_flg = True
                if chg_flg == True: #変更があった場合はもういっかいキューに戻す
                    queue.append((x,y))
                    #print(C[x][y][0])
        #print(C)
    #print(g[0],g[1])
    return min(C[g[0]][g[1]])

start, goal = (rs, cs), (rg, cg)
ans = bfs(start, goal,H, W, S)

if ans == 10**9:
    print(-1)
else:
    print(ans)