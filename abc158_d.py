S = list(input())
Q = int(input())

from collections import deque

q = deque(S)
rev = False

for i in range(Q):
    que = input()
    que = que.split(' ')

    if que[0] == '1':
        rev = not(rev)#反転
    else:
        if que[1] == '1':
            if rev == True:
                q.append(que[2])
            else:
                q.appendleft(que[2])
        
        else:#que[1] == '2"
            if rev == True:
                q.appendleft(que[2])
            else:
                q.append(que[2])

if rev == False:
    print(''.join(q))
else:
    q.reverse()
    print(''.join(q))

