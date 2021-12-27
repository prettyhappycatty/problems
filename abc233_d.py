# defaultdictをインポート
from collections import defaultdict
# 連想配列
#X=defaultdict(int)
#print(X)
X={}

N, K = map(int, input().split())

A = list(map(int, input().split()))

S = [0]
tmps = 0
for i in range(N):
    tmps += A[i]
    S.append(tmps)

cnt = 0
for r in range(1,N+1):
    if S[r-1] not in X.keys():
        X[S[r-1]] = 0 
    X[S[r-1]] += 1
    if S[r]-K in X.keys():
        cnt += X[S[r]-K]
#print(mp)
print(cnt)
