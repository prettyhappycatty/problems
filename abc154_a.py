S, T = input().split()
A, B = map(int, input().split())
U = input()

S_cnt = A
T_cnt = B

if U == S:
    S_cnt -= 1
else:
    T_cnt -= 1

print(S_cnt, T_cnt)
