import copy


masu = []
done = [[0 for _ in range(10)] for _ in range(10)]
neighbor = [(0,1),(1,0),(-1,0),(0,-1)]

#適当なスタートマスを探しておく
start_done = False
start_masu = (-1, -1)
for i in range(10):
    tmpA_s = input()
    tmpA = list(tmpA_s)
    masu.append(tmpA)
    if start_done == False and tmpA_s.find("o") > -1:
        j = tmpA_s.find("o")
        start_done = True
        start_masu = (i,j)


#print(masu, i,j)

#dfsのアルゴリズム
#終了条件：周りに判定していない場所がなかったらreturn 1:到達 0:未判定 -1:到達しない
#探索条件：4近傍

def dfs(i, j):
    if done[i][j] != 0:
        return
    if masu[i][j] == 'x':
        done[i][j] = -1
    else: #masu[i][j] == 'o':
        done[i][j] = 1
        for neigh in neighbor:
            nei_x = i + neigh[0]
            nei_y = j + neigh[1]
            #print(nei_x, nei_y)
            if nei_x < 0 or nei_x > 9 or nei_y < 0 or nei_y > 9:
                continue
            dfs(nei_x, nei_y)


masu_tmp = copy.deepcopy(masu) #tmpを保持しておく
done_tmp = copy.deepcopy(done) #tmpを保持しておく
for i in range(10):
    for j in range(10):
        masu = copy.deepcopy(masu_tmp)
        done = copy.deepcopy(done_tmp)
        if masu[i][j] == 'x':
            #対象1マス変えて全探索
            masu[i][j] = 'o'
            dfs(start_masu[0], start_masu[1])
        else:
            continue

        #陸に辿り着けるかを確認
        flg = True
        for k in range(10):
            for l in range(10):
                if done[l][k] != 1 and masu[l][k] == "o":
                    flg = False

        if flg == True:
            print("YES")
            exit()
        #print(done)


print("NO")