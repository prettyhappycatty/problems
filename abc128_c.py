N, M = map(int, input().split())

def countLightning(pat, k, s, p):
    cnt = 0

    for i in range(k):
        if pat[s[i]-1] == 1:
            cnt+=1
    #print(cnt, pat)
    return (cnt % 2 == p )

K = []
S = []
for i in range(M):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    s = tmp[1:]
    K.append(k)
    S.append(s)

p = list(map(int, input().split()))

import itertools
bi = list(itertools.product([0,1], repeat=N))
ans_cnt = 0
for i in range(len(bi)):
    l = list(bi[i])
    cnt = 0
    for j in range(M):
        if countLightning(l, K[j], S[j], p[j]):
            cnt+=1
    #print(cnt)
    if cnt == M:
        ans_cnt += 1

print(ans_cnt)