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
            


N, M = map(int, input().split())

ary = []

for i in range(M):
    a,b,y = map(int, input().split())
    ary.append((a-1,b-1,y)) # a, b, y

ary_sorted = sorted(ary, key=lambda x:x[2], reverse=True) # 新しい順につなげるため、新しい順のソート

uf = UnionFind(N)


Q = int(input())

Q_cnt = [0 for _ in range(Q)]
ary_q = {}
for i in range(Q):
     v, w= map(int, input().split())
     ary_q[i] = (v-1,w)


#print(ary_q)

ary_q_sorted = sorted(ary_q.items(), key=lambda x:x[1][1], reverse=True)

#print(ary_sorted)
#print(ary_q_sorted)

i = 0
j = 0
while i < M and j < Q:
    y1 = ary_sorted[i][2]
    c1 = ary_sorted[i][0]
    c2 = ary_sorted[i][1]
    #print(ary_sorted[i])
    y2 = ary_q_sorted[j][1][1]
    c3 = ary_q_sorted[j][1][0]
    idx = ary_q_sorted[j][0]
    #print(i,j, y1, y2)
    if y1 > y2:
        #print("union")
        uf.union(c1,c2)
        i += 1
    else:
        Q_cnt[idx] = uf.size(c3)
        j += 1

while j < Q:
    idx = ary_q_sorted[j][0]
    c3 = ary_q_sorted[j][1][0]
    Q_cnt[idx] = uf.size(c3)
    j += 1

for i in range(len(Q_cnt)):
    print(Q_cnt[i])