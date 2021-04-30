H, W = list(map(int, input().split()))

#4近傍で接続してるものがあるかないかを調べる
neigh = [(1, 0), (-1, 0), (0, -1), (0, 1)]

s = []

for i in range(H):
    tmp = list(input())
    s.append(tmp)

#print(s)
#print(H, W)

def checkNeighborBlack(x, y):#xの周りに少なくとも1つの#があること
    for nei in neigh:
        tmp_x, tmp_y = x + nei[0], y + nei[1]
        #print("tmp_x,tmp_y", tmp_x, tmp_y)
        if 0 <= tmp_x < H and 0 <= tmp_y < W and s[tmp_x][tmp_y] == '#':
            #print('true')
            return True
    #print('false')
    return False
    

flg = True
for i in range(H):
    if flg == False:
        break
    for j in range(W):
        if s[i][j] == '#':
            #print("i,j", i,j)
            flg = checkNeighborBlack(i, j)
            if flg == False:
                break

if flg == False:
    print('No')
else:
    print('Yes')