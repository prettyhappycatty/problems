#トポロジカルソート、DAG Directed Acyclic Graph
# むり
import sys
sys.setrecursionlimit(1000000)

N, M, K = map(int, input().split())


edges = []
for i in range(N):
    edges.append([])


# 始点の判定につかう入次数
indeg = [0]*N
for i in range(M):
    x, y = list(map(int, input().split()))
    edges[x-1].append(y-1)
    indeg[y-1] += 1

ans = [[] for _ in range(M)]
for i in range(N):
    ans[indeg[i]].append(i)

print(ans)

# 閉路のない有効グラフにはトポロジカルソートが存在する。
# length[i]: iを始点とするパスのうち、最も長いものの長さを管理。
length = [0] * N
done = [False] * N


def dfs(depth):
    #計算すみであれば値を返す
    if depth == N:
        return [i]
    # そうでなければ値を計算する
    length[i] = 0
    ary = []
    for j in edges[i]:
        ary.extend(dfs(j))
    
    done[i] = True
    return ary

# 視点全てについてrecを呼び出す
for i in ans[0]:
    print(dfs(i))

#print(indeg)
#print(done)
#print(length)