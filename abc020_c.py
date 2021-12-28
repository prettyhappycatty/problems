H, W, T = map(int, input().split())


S = []
for i in range(H):
    s = input()
    st = s.find("S")
    en = s.find("G")
    if st > -1:
        start = [i, st]
    if en > -1:
        goal = [i, en]
    S.append(list(s))
    

#print(S)

import queue
 
neigh = [(0, 1), (1, 0), (-1, 0), (0, -1)]


from heapq import heappop, heappush

#ダイクストラ法で最短距離を求める
def dijkstra(x):
    st = start
    hq = [(0, st[0], st[1])] #始点
    dist = [[10**9*W*H for _ in range(W)] for _ in range(H)]
    dist[st[0]][st[1]] = 0 #始点の距離
    seen = [[False for _ in range(W)] for _ in range(H)] #通ったかどうか
    #print(seen)
    #print(dist[0][0], dist[1][0])
    while hq:
        #print(hq)
        v = heappop(hq)
        #print(v)
        #print(a,v)
        if seen[v[1]][v[2]]:
            continue

        seen[v[1]][v[2]] = True
        
        for nei in neigh:
            nei_x = v[1] + nei[0]
            nei_y = v[2] + nei[1]
            #print(v[0],v[1],nei_x, nei_y)
            if nei_x < 0 or nei_y < 0 or nei_x >= H or nei_y >= W:
                continue
            #print(nei_x, nei_y, v[0],v[1])
            if S[nei_x][nei_y] == "#":
                tmp_dist = x
            else:
                tmp_dist = 1
            #print(nei_x,nei_y,v[0],v[1],"dist=", dist[nei_x][nei_y],dist[v[0]][v[1]],"tmp=",tmp_dist)
            if dist[nei_x][nei_y] > dist[v[1]][v[2]] + tmp_dist:
                #print(nei_x,nei_y, "updated!->", dist[nei_x][nei_y], "to",dist[v[0]][v[1]] + tmp_dist )
                dist[nei_x][nei_y] = dist[v[1]][v[2]] + tmp_dist
                heappush(hq, (dist[nei_x][nei_y], nei_x,nei_y))
            #print(nei_x,nei_y,v[0],v[1],"dist=", dist[nei_x][nei_y],dist[v[0]][v[1]],"tmp=",tmp_dist)

    return dist

en = goal

hi = T
lo = 1
if T == 2:
    ans = dijkstra(T)
    if ans[goal[0]][goal[1]] >= T:
        print(1)
        exit()
    else:
        print(2)
        exit()


while hi - lo > 1:
    mid = (hi+lo)//2
    ans = dijkstra(mid)
    #print(mid, ans, ans[goal[0]][goal[1]])
#    print(ans)
    if ans[goal[0]][goal[1]] <= T:
        #まだ増やせる
        lo = mid
    else:
        #減らさないとダメ
        hi = mid
    #print(lo, hi)

print(lo)
