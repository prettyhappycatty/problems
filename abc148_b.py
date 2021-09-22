N = int(input())
S, T = list(input().split())

ans = ""
for i in range(len(S)):
    ans +=S[i]
    ans +=T[i]

print(ans)

