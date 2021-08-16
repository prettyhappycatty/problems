

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
            
N = int(input())
ary = []
for i in range(N-1):
    u, v, w = map(int, input().split())
    ary.append((u-1,v-1,w))

ary_sorted = sorted(ary, key=lambda x:x[2],reverse=False)

#print(ary_sorted)

uf = UnionFind(N)

ans = 0
for i in range(N-1):
    w = ary_sorted[i][2]
    u = ary_sorted[i][0]
    v = ary_sorted[i][1]
    ans += w*uf.size(u)*uf.size(v)
    uf.union(u,v)

print(ans)
#print(uf.par)
    
