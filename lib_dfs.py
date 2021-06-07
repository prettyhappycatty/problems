import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())#N個の都市、M個の道

A, B = [],[]
connect =[[] for i in range(N)]

for i in range(M):#接続のリストを作る
    A_tmp, B_tmp=map(int,input().split())
    connect[A_tmp-1].append(B_tmp-1)


#print(connect)

# dfs
def dfs(v):
  if temp[v]: return  # 同じ頂点を2度以上調べないためのreturn
  temp[v]=True #到達した都市をTrueにする
  for vv in connect[v]:
       dfs(vv)

ans=0
# 都市iからスタートする場合
for i in range(N):
	temp=[False]*N # 初期化、すべての都市を到達不可能とみなす
	# temp[j] は都市jに到達可能かどうかを表す
	dfs(i)
	ans+=sum(temp)#Trueの個数をたす

print(ans)