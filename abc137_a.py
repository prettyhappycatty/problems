A, B = map(int, input().split())

m = -101

m = max(A+B, m)
m = max(A-B, m)
m = max(A*B, m)

print(m)