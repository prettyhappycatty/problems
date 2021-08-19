A, B = input().split()

a,b = 0,0
for i in range(3):
    a += int(A[i])
    b += int(B[i])
if a > b:
    print(a)
else:
    print(b)