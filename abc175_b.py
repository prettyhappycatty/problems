N = int(input())
L = list(map(int, input().split()))

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            max_L = max(L[i], L[j], L[k])
            min_L = min(L[i], L[j], L[k])
            mid_L = L[i] + L[j] + L[k] - max_L - min_L

            if max_L < min_L + mid_L:
                cnt += 1

print(cnt)