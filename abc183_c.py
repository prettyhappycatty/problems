import itertools

N, K = map(int, input().split())

T = []

for i in range(N):
    tmpT = list(map(int, input().split()))
    T.append(tmpT)

#print(T)
a = list(itertools.permutations(range(N-1), N-1))
#print(len(a))
cnt = 0

for j in range(len(a)):
    p = a[j]
    #print(p)
    bef = 0
    tmp = 0
    for i in range(0, N-1):
        now = p[i]
    #    print(bef, now+1)
        dist = T[now+1][bef]
        tmp += dist
        bef = now+1
    #print(bef,0)
    tmp += T[bef][0]
    #print(tmp)
    if tmp == K:
        cnt += 1

print(cnt)
