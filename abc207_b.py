A, B, C, D = map(int, input().split())
red = 0

#x回後 red = C*x  A = A + B*x
#D*(C*x) < A+B*x
#A > (C*D - B)*x

if C*D - B <= 0:
    print(-1)
    exit()

times = 0
while A > D*red:
    A += B
    red += C
    times += 1
print(times)
