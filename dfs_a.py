import sys
sys.setrecursionlimit(10000000)

H, W = map(int, input().split())

C = []
F = [[-1 for _ in range(W)] for _ in range(H)]
#s = (-1,-1)
#g = (-1,-1)
for i in range(H):
    tmp = input()
    C.append(tmp)
    #print(len(tmp))
    for j in range(len(tmp)):
        #print(tmp[j])
        if tmp[j] == "s":
            s = (i,j)
        elif tmp[j] == "g":
            g = (i,j)

#print(s,g)
#print(C)
neighbor = [(0,1),(1,0),(0,-1),(-1,0)]

def dfs(current):
    for nei in neighbor:
        x = current[0] + nei[0]
        y = current[1] + nei[1]
        #print(F)
        if x > -1 and y > -1 and y < W and x < H:
            if F[x][y] > -1:
                continue
            #print(F)
            if C[x][y] == ".":
                F[x][y] =1
                #print("=.")
                dfs((x,y))
            elif C[x][y] == "#":
                F[x][y] = 2
            elif C[x][y] == "g":
                print("Yes")
                exit()
            #print("c,f",C[x][y],F[x][y])

dfs(s)
#for i in range(len(F)):
#    print(F[i])

#print(C)
if F[g[0]][g[1]] == -1:
    print("No")