import sys
sys.setrecursionlimit(400000000)

H, W= map(int, input().split())

A = []
memo =  [['' for i in range(W)] for j in range(H)]
#print(memo)

def cell(x, y, ary):
    #print(ary)
    if ary[x][y] == "+":
        return 1
    elif ary[x][y] == "-":
        return -1
    return 

def q(ary, memo):
    if H == 1 and W == 1:
        memo[0][0] = 0
        return memo
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            #print(i,j)
            #print(cell(i,j, ary))
            fugou = (i+j) % 2
            times = (-1)**fugou
            if j+1 == len(ary[0]) and i+1 == len(ary):
                #memo[i][j] = times*cell(i,j,ary)
                memo[i][j] = 0
                continue
            elif j+1 >= len(ary[0]) :
                memo[i][j] = memo[i+1][j] + times *cell(i+1,j,ary)
            elif i+1  >= len(ary):
                memo[i][j] = memo[i][j+1]+ times *cell(i,j+1,ary)
            else:
                if fugou > 0:
                    memo[i][j] = min(memo[i+1][j]+ times *cell(i+1,j,ary), memo[i][j+1]+ times *cell(i,j+1,ary))
                else:
                    memo[i][j] = max(memo[i+1][j]+ times *cell(i+1,j,ary), memo[i][j+1]+ times *cell(i,j+1,ary))
    return memo


for i in range(H):
    tmp_A= input()
    A.append(tmp_A)

cnt_memo = q(A,memo)

#print(cnt_memo)
#print(cnt_memo)

if cnt_memo[0][0] > 0:
    print("Takahashi")
elif cnt_memo[0][0] < 0:
    print("Aoki")
else:
    print("Draw")