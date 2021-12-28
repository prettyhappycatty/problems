#個数つきUnionFind

class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納。par[x] == xの時そのノードは根
        self.n = n
        self.par = [-1 for _ in range(n+1)]
        # 木の高さを格納する（初期状態では0）
        self.rank = [0] * (n+1)
        self.datamax = list(range(n))

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
        x_tmp, y_tmp = x,y
        # 根を探す
        if y_tmp == self.n:
            y_tmp= 0
        x = self.find(x_tmp)
        y = self.find(y_tmp)
        
        self.datamax[x] = self.datamax[y]

        if x == y:
            return 0
        else:
            if self.par[x] > self.par[y]:
                x,y = y,x
            self.par[x] += self.par[y]
            self.par[y] = x
            

#====
Q = int(input())
MOD = 1048576
#MOD = 100

uf = UnionFind(MOD)

A = [-1 for _ in range(MOD)]

def query1(x):
    h = uf.find(x % MOD)
    A[uf.datamax[h]] = x
    uf.union(uf.datamax[h], uf.datamax[h]+1)
    #print(uf.datamax)

def query2(x):
    return A[x % MOD]

for i in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        query1(x)
    else:
        print(query2(x))

#print(uf.datamax[0:40])
#print(A[0:40])