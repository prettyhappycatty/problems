N = int(input())
S = input()

if N % 2 == 1:
    print(-1)
    exit()

cnt = 0
for i in range(N//2):
    if S[i] != S[N//2 + i]:
        cnt += 1

print(cnt)