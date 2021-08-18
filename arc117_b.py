N = int(input())
A = list(map(int, input().split()))

A.sort()

#print(A)

mul = A[0] + 1
mul %= 1000000007
for i in range(0, N-1):
    mul *= (A[i+1]-A[i]+1) 
    mul %= 1000000007

print(mul)