#単純なbfs

H, W = map(int, input().split())
S = []
for i in range(H):
    tmpS = input()
    S.append(tmpS)


from collections import deque
def check_s_g(S):
    for i in range(len(S)):
        for j in range(len(S[0])):
            if S[i][j] == "s":
                s = (i,j)
            if S[i][j] == "g":
                g = (i,j)
    return s, g

neigh = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(now, g, h, w, S):
    C = [[-1 for _ in range(W)] for _ in range(H)]#距離の初期化
    queue = deque([now])
    C[now[0]][now[1]] = 0 # 自分との距離は0
    while queue:
        print(queue)
        v = queue.popleft()
        print(v)
        for nei in neigh:#g[v]:
            x = v[0]+nei[0]
            y = v[1]+nei[1]
            if 0<= x < h and 0<= y < w and C[x][y] == -1 and S[x][y] != "#":
                C[x][y] = C[v[0]][v[1]]+1
                queue.append((x,y))
        print(C)
    return C[g[0]][g[1]]

#---ここから
start, goal = check_s_g(S)
print(S[1][1])
print(bfs(start, goal,H, W, S))