
plus_matrix = [[0 for _ in range(10)] for _ in range(10)]
mul_matrix = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    ii = i
    for j in range(10):
        jj = j
        plus_matrix[i][j] = (ii+jj)%10
        mul_matrix[i][j] = (ii*jj)%10

#print("plus")
#for i in range(10):
#    print(plus_matrix[i])

#print("mul")
#for i in range(10):
#    print(mul_matrix[i])

from collections import deque

N = int(input())
A = list(map(int, input().split()))


import itertools
from collections import deque
#0=F 1=G
pat = list(itertools.product([0,1],repeat=N-1))
ans = [0 for i in range(10)]
for i in range(len(pat)):
    patt = pat[i]
    #print(patt)
    pat_idx = 0
    que = deque(A)
    while pat_idx < len(patt):
        a = que.popleft()
        b = que.popleft()
        #print(patt[pat_idx])
        if patt[pat_idx] == 0:#plusをする
            que.appendleft(plus_matrix[a][b])
        else:
            que.appendleft(mul_matrix[a][b])
        #print(que)
        pat_idx += 1
    #print(que)
    ans[que[0]] += 1

for i in range(len(ans)):
    print(ans[i])