H, W = map(int, input().split())
Q = int(input())

neigh = [(0,1), (1, 0), (-1,0),(0,-1)]


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
        print(self.par)
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

uf = UnionFind((H+1)*(W))

for i in range(Q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 1 :
        r1, c1 = tmp[1],tmp[2]
        for s in neigh:
            r = r1 + s[0]
            c = c1 + s[1]
            if r < 0 or c < 0 or r >= W or c >= H:
                continue
            if uf.size(r*W + c) != 1:#つながっている場合
                uf.union(r*W + c, r1*W + c1)
    else:#==2
        r1, c1, r2, c2 = tmp[1],tmp[2],tmp[3],tmp[4]
        if uf.same_check(r1*W +c1, r2*W + c2):
            print("Yes")
        else:
            print("No")