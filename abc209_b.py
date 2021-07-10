N, X = map(int, input().split())

A = list(map(int,input().split()))

sumA = 0
for i in range(len(A)):
    if i % 2 == 1:#偶数番目
        sumA += A[i] - 1
    else:
        sumA += A[i]

#print(X, sumA)

if X >= sumA:
    print("Yes")
else:
    print("No")

