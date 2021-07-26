from collections import deque

h,w = map(int, input().split())

cxy = []

white = 0
for i in range(h):
    tmp = list(input())
    #print(tmp[1])
    cxy.append(tmp)
    white += tmp.count(".")

#print(white)
ssx, ssy = 0,0
ggx, ggy = h-1,w-1

INF = -1

length = [[INF for j in range(w)]for i in range(h)]
visited = [[0 for j in range(w)]for i in range(h)]

length[ssx][ssy] = 0
visited[ssx][ssy] = 1
#print(ans)

neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]

q = deque([])

q.append((ssx, ssy))

if cxy[ssx][ssy] == "#" or cxy[ggx][ggy] == "#":
    print(-1)
    exit()

while q:
    s = q.popleft()
    #print(neigh)
    for nei in neigh:
        #print(nei[0],nei[1])
        x = s[0] + nei[0]
        y = s[1] + nei[1]
        #print(x,y)
        if x >= h or y >=w or x < 0 or y < 0:
            continue
        #print(cxy[x][y])
        if cxy[x][y] =="#":#壁
            visited[x][y] = 1
            continue
        elif visited[x][y] == 1:
            continue
 #       print(length)
        if visited[x][y] == 0: #未決定
            length[x][y] = length[s[0]][s[1]] + 1
            visited[x][y] = 1
            #print(x,y)
            if x == ggx and y == ggy:
                print(white - 1 - length[x][y])
                exit()
            else:
                q.append((x,y))
                #print(cxy[x][y])


if length[h-1][w-1] == INF:
    print(-1)
else:
    print(white-length[h-1][w-1]) 