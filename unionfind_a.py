

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
            
N, Q = map(int, input().split())
ary = []
for i in range(Q):
    p, a, b = map(int, input().split())
    ary.append((p, a-1,b-1))

#ary_sorted = sorted(ary, key=lambda x:x[2],reverse=False)

#print(ary_sorted)

uf = UnionFind(N)

ans = 0
for i in range(Q):
    p = ary[i][0]
    a = ary[i][1]
    b = ary[i][2]
    #print(p,a,b)
    #ans += w*uf.size(u)*uf.size(v)
    if p == 0:
        uf.union(a,b)
    else:
        #print(uf.find(a), uf.find(b))
        if uf.find(a) == uf.find(b):
            print("Yes")
        else:
            print("No")

    
