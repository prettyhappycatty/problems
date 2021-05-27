import sys
sys.setrecursionlimit(200000)

A, B, K = map(int, input().split())

N = A + B

ans = ""

memo = [[-1 for j in range(1010)] for i in range(1010)]

def aCb(a, b):
    #print(a,b)
    if b == 0 or a == b:
         return 1
    if 0 <= memo[a][b]:
         return memo[a][b]
    memo[a][b] = aCb(a - 1, b - 1) + aCb(a - 1, b)
    return memo[a][b]

for i in range(N):
    if 0 < A:
        if (K <= aCb(A + B - 1, B)) :
                ans += "a"
                A -= 1
        else:
                #print(K, aCb(A + B - 1, B))
                ans += "b"
                K -= aCb(A + B - 1, B)
                B -= 1
    else:
        ans += "b"
        B -= 1

print(ans)