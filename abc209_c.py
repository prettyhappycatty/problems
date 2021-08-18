N = int(input())
C = list(map(int, input().split()))

SOSUU = 1000000009
#print(SOSUU)

C.sort()
#print(C)

mul = 1
for i in range(N):
    mul = mul * max(0, C[i] - i) % 1000000007
print(mul % SOSUU)