import sys
sys.setrecursionlimit(100000)

N = int(input())

B = []
C = []

for i in range(N-1):
    B.append(int(input())-1)
    C.append(-1)

#print(B)

G = {}

for i in range(1, N):
    if B[i-1] not in G.keys():
        G[B[i-1]] = []
    G[B[i-1]].append(i)

#print(G)

def dfs(i):

    if i not in G:#部下がいない場合
        return 1
    else:
        values = []
        for j in G[i]:
            values.append(dfs(j))
        return max(values)+min(values)+1

print(dfs(0))
