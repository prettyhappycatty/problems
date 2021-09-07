N = int(input())

A = list(map(int, input().split())) #indexが2から始まる
cnt = {}
for i in range(1, N+1):
    cnt[i] = 0

for i in range(1, N):
    cnt[A[i-1]] += 1

for i in range(1, N+1):
    print(cnt[i])

