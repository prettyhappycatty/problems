Q, H, S, D=list(map(int, input().split()))
N = int(input())

S_min = S
if 4*Q < S:
    S_min = 4*Q

if 2*H < S_min:
    S_min = 2*H

if 2 * S_min > D:
    print((N//2)*D + (N % 2) * S_min)
else:
    print (N*S_min)