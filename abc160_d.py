#要復習

inf = 10**9
ans = [1 for _ in range(2020)]

N, X ,Y = map(int, input().split())
X -=1
Y -=1
for i in range(N):
    for j in range(i+1, N):
        k = inf

        k = min(k, j - i)
        k = min(k, abs(X - i) + abs(Y - j) + 1)

        ans[k] += 1

for k in range(1, N):
    print(ans[k]-1)
