import sys
sys.setrecursionlimit(1000000)

H, W = map(int, input().split())

S = []
start_h, start_y = 0,0
S.append(["#"]*(W+2))
for i in range(H):
    tmpS = ["#"]
    tmpS.extend(list(input()))
    tmpS.append("#")
    S.append(tmpS)
S.append(["#"]*(W+2))


#print(S)

ans = [[0 for i in range(W+2)] for j in range(H+2)]

#print(ans)

neigh = [(0,1),(1,0)]

mmax = [1]

def dfs(i, j):
    #print(i,j,"->")
    if S[i+neigh[0][0]][j+neigh[0][1]] != "#" and ans[i][j]+1 > ans[i+neigh[0][0]][j+neigh[0][1]]:
        ans[i+neigh[0][0]][j+neigh[0][1]] = ans[i][j]+1
        mmax[0] = max(mmax[0],ans[i][j]+1)
        dfs(i+neigh[0][0],j+neigh[0][1])

    if S[i+neigh[1][0]][j+neigh[1][1]] != "#" and ans[i][j]+1 >  ans[i+neigh[1][0]][j+neigh[1][1]]:
        ans[i+neigh[1][0]][j+neigh[1][1]] = ans[i][j]+1
        mmax[0] = max(mmax[0],ans[i][j]+1)
        dfs(i+neigh[1][0],j+neigh[1][1])
    return 

ans[1][1] = 1
dfs(1,1)

print(mmax[0])