N, Q = map(int, input().split())
A = list(map(int, input().split()))

start = 0
for i in range(Q):
    tmpT, tmpX, tmpY = map(int, input().split())
    tx = (tmpX - 1 - start + N) % N
    ty = (tmpY - 1 - start + N) % N
    #print(start, tx, ty, tmpT, tmpX, tmpY)
    if tmpT == 1:
        tmp = A[tx]
        A[tx] = A[ty]
        A[ty] = tmp
    elif tmpT == 2:
        start = (start + 1) % N
    else:#tmpT == 3
        print(A[tx])


