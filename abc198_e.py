import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
C = list(map(int, input().split()))

connected = [[] for _ in range(N)]
a_list = []
b_list = []

for i in range(N-1):
    a, b = list(map(int, input().split()))
    a_list.append(a-1)
    b_list.append(b-1)

#print(connected)

for i in range(N-1):
    #print(len(connected),i, N-1)
    #print(i, a_list[i], b_list[i], a_list[i]-1, b_list[i]-1)
    connected[a_list[i]].append(b_list[i])
    connected[b_list[i]].append(a_list[i])

#print(connected)#dfsの元となるやつ
    
cnt=[0] * 100001
ans=[0] * 100001

#print(len(connected))

def dfs(cu, pa=-1): #cu=0 C[cu]:各色の数カウント
    if cnt[C[cu]] == 0:
        ans[cu] = 1
 
    for to in connected[cu]: #特定のノードに接続されているノードについてループ
        if to != pa:
            cnt[C[cu]] += 1 #i=cuの色の数を1増やす(頂点に侵入時)
            dfs(to, cu)
            cnt[C[cu]] -= 1 #i=cuの色の数を1増やす(頂点からの退出時)
 
dfs(0)

for i in range(N):
    if ans[i] == 1:
        print(i+1)
            
#todo
