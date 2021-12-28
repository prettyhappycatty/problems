N = int(input())
A = list(map(int, input().split()))

ans = 0
asum = 0
dist = 0
asummax = 0

for i in range(N):
    asum += A[i]
    asummax = max(asum, asummax)
    ans = max(dist+asummax, ans)
    dist += asum

print(ans)