N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

#print(A)
#print(B)

s = 0
for i in range(N):
    dist = abs(A[i]-B[i])
    s += dist

print(s)