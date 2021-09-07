N = int(input())
A = list(map(int, input().split()))

cnt = {}
for i in range(N):
    if A[i] not in cnt.keys():
        cnt[A[i]] = 0
    cnt[A[i]] += 1
    if cnt[A[i]] > 1:
        print("NO")
        exit()

print("YES")