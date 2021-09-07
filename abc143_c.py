N = int(input())
S = input()

bef = ""
cnt = 0
for i in range(N):
    if bef != S[i]:
        cnt += 1
    bef = S[i]
print(cnt)
