A, B, C = map(int, input().split())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

cal_gcd = gcd(gcd(A,B),C)
A = A//cal_gcd
B = B//cal_gcd
C = C//cal_gcd

print(A-1 + B -1 + C -1)


