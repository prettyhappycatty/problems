N = int(input())
A = list(map(int, input().split()))

DP = [10**5+1 for _ in range(N)]
DP[0] = 0
DP[1] = abs(A[1]-A[0])

for i in range(2, N):
    DP[i] = min(DP[i-1]+abs(A[i]-A[i-1]), DP[i-2]+abs(A[i]-A[i-2]))

print(DP[N-1])

