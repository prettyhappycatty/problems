A, B = input().split()

A = int(A)
B = B.split(".")
B = int(B[0])*100+int(B[1])
B = int(B)

print(int(A*B // 100))
