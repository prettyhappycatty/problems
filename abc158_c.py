import math

A, B = list(map(int, input().split()))


f_A = math.ceil(A/0.08)
f_B = math.ceil(B/0.1)
c_A = math.floor((A+1)/0.08)
c_B = math.floor((B+1)/0.1)
#print(f_A, c_A, f_B, c_B)

flg = 0#重なり有無
if f_A <= f_B and f_B < c_A :#重なり、Bの最小値が答えのパターン
    flg = 1
    f = f_B
elif f_B <= f_A and f_A < c_B:#重なり、Aの最小値が答えのパターン
    flg = 1
    f = f_A

if flg == 1:
    print(f)
else:
    print(-1)
