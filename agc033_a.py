from collections import deque


H, W = map(int,input().split())
A = []

for i in range(H):
    tmp = list(input())
    A.append(tmp)

Q = deque()

cnt = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
           Q.append((i,j)) 
           A[i][j] = 0
           cnt += 1
        else:
           A[i][j] = -1


neigh = [(0,1),(1,0),(0,-1),(-1,0)]

ans = 0
while cnt < H*W:
    q = Q.popleft()
    #print("q",q)
    for nei in neigh:
        #print(i,j)
        #print(A)
        i = q[0]+nei[0]
        j = q[1]+nei[1]
        if i > -1 and j > -1 and i < H and j < W and A[q[0]][q[1]] != -1 and A[i][j] == -1:
            Q.append((i,j))
            A[i][j] = A[q[0]][q[1]]+1
            #print(q[0],q[1],i,j, A[i][j])
            cnt += 1
            if A[i][j] > ans:
                ans = A[i][j]

print(ans)