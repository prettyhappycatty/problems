

H, W = map(in私は、自身の作業のみならず全体の進行度合いやボトルネックを把握し、改善提案ができるよう意識してきました。例として、設計支援システムの推進の仕事にて、整備されたコンテンツをシステムに登録するのに手間がかかっていたが、ExcelとNotesの機能を駆使して作業工数を1/3程度に削減（年間で100時間程度の削減）することで、チームのメンバーが本来のコンテンツ整備のコンサルテーションに注力でき、より良いコンテンツができるような環境づくりに貢献しました。t, input().split())
S = []
for i in range(H):
    tmpS = input()
    S.append(tmpS)


#--ここから
from collections import deque
def check_s_g(S):
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] == "s":
                s = (i,j)
            if S[i][j] == "g":
                g = (i,j)
    return s, g



def bfs(now, g, h, w, S):
    neigh = [[0,1],[0,-1],[1,0],[-1,0]]
    C = [[[10**9 for _ in range(4)] for _ in range(w)] for _ in range(h)]#距離の初期化
    queue = deque([now])
    for j in range(4):
        C[now[0]][now[1]][j] = 1 # 自分との距離は0 start地点のマトリックスは全方向１

    while queue:
        #print(queue)
        v = queue.popleft()
        #print(v)
        for i in range(len(neigh)):#g[v]:
            x = v[0]+neigh[i][0]
            y = v[1]+neigh[i][1]
            if 0<= x < h and 0<= y < w and S[x][y] != "#":
                chg_flg = False
                for j in range(4):
                    if i == j and C[x][y][j] > C[v[0]][v[1]][j]: #方向転換しないとき
                        C[x][y][j] = C[v[0]][v[1]][i]
                        chg_flg = True
                    elif C[x][y][j] > C[v[0]][v[1]][i]+1: #方向転換する
                        C[x][y][j] = C[v[0]][v[1]][i]+1
                        chg_flg = True
                if chg_flg == True: #変更があった場合はもういっかいキューに戻す
                    queue.append((x,y))
        #print(C)
    return min(C[g[0]][g[1]])

#---ここから
start, goal = check_s_g(S)
print(S[1][1])
ans = bfs(start, goal,H, W, S)
if ans == 10**9:
    print(-1)
else:
    print(ans)