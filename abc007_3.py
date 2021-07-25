import queue

R,C = map(int, input().split())
sx,sy = map(int, input().split())
gx,gy = map(int, input().split())

cxy = []

ans = [[-1 for _ in range(C)] for _ in range(R)]

for i in range(R):
    tmp = list(input())
    #print(tmp[1])
    cxy.append(tmp)

ssx, ssy = sx-1,sy-1
ggx, ggy = gx-1,gy-1

ans[ssx][ssy] = 0


#print(ans)

neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]

q = queue.Queue()

q.put((ssx, ssy))

while q:
    s = q.get()
    #print(neigh)
    for nei in neigh:
        #print(nei[0],nei[1])
        x = s[0] + nei[0]
        y = s[1] + nei[1]
        #print(x,y)
        if x >= R or y >=C or x < 0 or y < 0:
            continue
        #print(cxy[x][y])
        if cxy[x][y] =="#":#壁
#            print("#",x,y)
            ans[x][y] == -2
            continue
        else:
#            print(".",x,y)
            if ans[x][y] == -1: #未決定
                ans[x][y] = ans[s[0]][s[1]] + 1
                q.put((x,y))
                if x == ggx and y == ggy:
                    print(ans[x][y])
                    exit()

print(ans)