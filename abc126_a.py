N, K = map(int, input().split())
S = list(input())

A = []
for i in range(N):
    if i != K-1:
        A.append(S[i])
    else:
        a = S[i].lower()
        A.append(a)

print(''.join(A))