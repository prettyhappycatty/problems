import itertools
import math


N = int(input())
t=[i for i in range(1, N+1)]
itertools.permutations(t)
T = list(itertools.permutations(t))

P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

flg = 0
P_order = 0
Q_order = 0
for i in range(math.factorial(N)):
    #print(T[i], Q, P)
    if P == T[i]:
        P_order = i+1
        flg += 1
    if Q == T[i]:
        Q_order = i+1
        flg +=1
    if flg == 2:
        break

print(abs(P_order-Q_order))