R, G, B, N = list(map(int, input().split()))

cnt = 0 
for i in range(N//R + 1):
    for j in range(N//G + 1):
        k = i * R + j * G
        if N >= k and (N - k) % B == 0:
            cnt += 1
 
print(cnt)