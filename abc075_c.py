


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.par = [-1 for _ in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n+1)

        # 検索
    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
         # 根でないなら、親の要素で再検索
        else:
            # 走査していく過程で親を書き換える
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])
    

    def size(self,x):
        return -self.par[self.find(x)]

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

        # 併合
    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        #print(x,y)
        if x == y:
            return 0
        else:
            if self.par[x] > self.par[y]:
                x,y = y,x
            self.par[x] += self.par[y]
            self.par[y] = x
            

N, M = map(int, input().split())

lst = []

for i in range(M):
    a, b = map(int, input().split())
    lst.append((a-1,b-1))

cnt = 0
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if i != j: #自分自身以外の連結グラフを計算
            a = lst[j][0]
            b = lst[j][1]
            uf.union(a,b)
    if uf.same_check(lst[i][0],lst[i][1]) == False:
        cnt += 1

print(cnt)