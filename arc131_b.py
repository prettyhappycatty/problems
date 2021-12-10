H, W = map(int, input().split())

g = []
for i in range(H):
    tmpg = list(input())
    g.append(tmpg)
    #print(tmpg)

neigh = [(0,1), (0,-1),(1, 0), (-1,0)]

for i in range(H):
    for j in range(W):
        if g[i][j] != ".":
            continue

        cols = {"1":False, "2":False, "3":False, "4":False, "5":False}

        for n in neigh:
            ip = n[0]
            jp = n[1]
            #print(i, j, i + ip, j + jp,g[i+ip][j+jp])
            if i + ip < H and i + ip >= 0 and j+jp < W and j+jp >= 0:
                #print(i, j, i + ip, j + jp,g[i+ip][j+jp])
                cols[g[i+ip][j+jp]] = True
        #print(cols)
        for k,v in cols.items():
            if v == False:
                g[i][j] = k
                #print(k)
                break

for i in range(H):
    print(''.join(g[i]))


