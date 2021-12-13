from collections import deque, defaultdict

N, M = map(int, input().split())

ab = []
g = [[] for _ in range(N)]
cnt = [0 for _ in range(N)]
for _ in range(M):
    a,b = map(int, input().split())
    ab.append(tuple((a,b)))
    g[a-1].append(b-1)
    cnt[a-1] += 1
    g[b-1].append(a-1)
    cnt[b-1] += 1

#print(g)

#2人以上の隣条件がある場合にNG
for i in range(N):
    if cnt[i] > 2:
        print("No")
        exit()

#閉路を検出
def getRoot(i):
    lst = [i]
    GG = g[i]
    while len(GG) > 1:
        for j in GG:
            #print(j,GG, lst)
            if j == i:
                continue
            else:#接続していないもう一方
               if j in lst:
                   #print(j,lst)
                   return False
               else:
                   lst.append(j)
                   GG = g[j]
                   i = j
    return True

for i in range(N):
    #print("i=",i)
    if getRoot(i) == False:
        print("No")
        exit()

print("Yes")
    


