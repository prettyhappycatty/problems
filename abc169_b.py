N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()

mul = 1
for i in range(N):
    mul *= A[i]
    if mul > 10**18:
        print(-1)
        exit()

print(mul)