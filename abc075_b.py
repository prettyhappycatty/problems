H, W = list(map(int, input().split()))

around_x = {-1, 0, 1}
around_y = {-1, 0, 1}

def checkBomb(ary, x, y, h, w):
    if x <= -1 or x >= w or y <= -1 or y >= h:
        return False
    else:
        if ary[x][y] == '#':
            return True 

ary = []
for i in range(H):
    tmp = input()
    ary.append(tmp)

ary2 = []
for i in range(H):
    tmp_str = ''
    for j in range(W):
        cnt = 0
        #print(i, j, ary[i][j])
        if ary[i][j] == '#':
            tmp_str += '#'
        else:
            for k in around_x:
                for l in around_y:
                    #print('a:',i+k, j+l, W, H)
                    if checkBomb(ary, i+k, j+l, W, H) == True:
                        cnt +=1
            
            tmp_str += str(cnt)
            #print('b;', i, j, cnt)
    ary2.append(tmp_str)
                
for i in range(len(ary2)):
    print(ary2[i])