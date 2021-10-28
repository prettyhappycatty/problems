N, K, S = map(int, input().split())

ans = []
for i in range(K):
    ans.append(S)
for i in range(K, N):
    if S == 10**9:
        ans.append(1)
    else:
        ans.append(S+1)

a = ' '.join(map(str,ans))
print(a)