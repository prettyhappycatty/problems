N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

cnt = 0
for i in range(K):
    cnt += p[i]

print(cnt)
