N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
pre = -2
for i in range(N):
    eat = A[i] - 1
    ans += B[eat]
    #print(B[eat])
    if pre == eat-1:
        ans += C[eat-1]
        #print(C[eat-1])
    pre = eat

print(ans)