K = int(input())
S = input()

if len(S) > K:
    ret = S[0:K] + "..."
else:
    ret = S

print(ret)