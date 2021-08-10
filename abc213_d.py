#オイラーツアー, dfs

import sys
sys.setrecursionlimit(1000000)

N = int(input())#N個の都市、M個の道

A, B = [],[]
connect =[[] for i in range(N)]
history = []
temp=[0]*N # 初期化、すべての都市を到達不可能とみなす
# dfs
def dfs(v, pre):
    history.append(v+1)
    #print(connect[v])
    for vv in connect[v]:
        if vv != pre:
            #history.append(vv+1)
            flg = dfs(vv, v)
            history.append(v+1)

def main():
    for _ in range(N-1):#接続のリストを作る
        A_tmp, B_tmp=map(int,input().split())
        connect[A_tmp-1].append(B_tmp-1)
        connect[B_tmp-1].append(A_tmp-1)

    for i in range(len(connect)):
        l = sorted(connect[i])
        connect[i] = l
    #connect = connect2

    #print(connect)
    dfs(0,-1)

    print(*history)

if __name__ == "__main__":
    main()