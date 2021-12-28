import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
A = []
B = []

ans = set()

g = [[] for _ in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  g[a-1].append(b-1)

#print(g)

def dfs(i):#iからスタートしてたどり着ける場所をans=set()に入れる
  if temp[i]:
    return
  temp[i] = True
  for j in g[i]:
      dfs(j)

cnt = 0
for i in range(N):
  temp=[False]*N # 初期化、すべての都市を到達不可能とみなす
  dfs(i)
  cnt += sum(temp)
  #print(i, len(ans))
#print(ans)
print(cnt)

