N = int(input())

S = {}
for i in range(N):
    u = input()
    if u not in S.keys():
        S[u] = 0
    S[u] += 1

S_sort = sorted(S.items(), key=lambda x:x[1],reverse=True)

print(S_sort[0][0])