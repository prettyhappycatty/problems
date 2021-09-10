N = int(input())

cnt = 0
for A in range(1, N):
    B = (N-1) // A
    cnt += B

print(cnt)