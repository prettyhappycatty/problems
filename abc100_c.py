N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    cnt_i = 0
    while A[i] % 2 == 0:
        cnt_i += 1
        A[i] = A[i] // 2
    cnt += cnt_i

print(cnt)