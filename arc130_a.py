N = int(input())
S = input()

bef = ""
idx = -1
cnt_set = []
for i in range(N):
    if bef != S[i]:
        idx += 1
        cnt_set.append(1)
    else:
        cnt_set[idx] += 1
    bef = S[i]

#print(cnt_set)

ans = 0
for i in range(len(cnt_set)):
    if cnt_set[i] >= 2:
        ans += cnt_set[i] * (cnt_set[i] -1) // 2

print(ans)