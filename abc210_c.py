import copy

N, K = map(int, input().split())
c = list(map(int, input().split()))

tmp = {}
colcnt = 0
maxcolcnt = 0
for i in range(0, K):
    if c[i] not in tmp.keys():
        tmp[c[i]] = 0
        colcnt += 1
    tmp[c[i]] += 1

if K == N:
    print(colcnt)
    exit()
#print(tmp)

maxcolcnt = colcnt
for i in range(K, N):
    if c[i] not in tmp.keys() or tmp[c[i]] == 0:
        tmp[c[i]] = 0
        colcnt += 1
    tmp[c[i]] += 1
#    print(tmp, c[i])
    if tmp[c[i-K]] == 1:
        colcnt -= 1
        tmp[c[i-K]] = 0
    else:
        tmp[c[i-K]] -= 1
#    print(tmp, c[i-K])
#    print(colcnt)
    if maxcolcnt < colcnt:
        maxcolcnt = colcnt

print(maxcolcnt)
