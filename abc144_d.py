import math
PI = 3.141592

a, b, x = map(int, input().split())

#傾きy度とした時に入ることのできる退席
sol_half = a*a*b /2

if x < sol_half :
    ans = math.atan(a*b*b / (2.0*x))
else:
    ans = math.atan((2.0*b-2.0*x/(a*a))/a)

#print(sol_half, ans)

ans = ans / PI*180
print(ans)