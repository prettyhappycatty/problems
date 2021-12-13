#UnionFindでの閉路の検出

class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

n, m = map(int, input().split())
ab = {tuple(map(int, input().split())) for _ in range(m)}

uf = UnionFind(n+1)
l = [0]*(n+1)
for a, b in ab:
  l[a] += 1
  l[b] += 1
  if uf.union(a, b) == False:#すでに同じグループに存在している場合
    print('No')
    exit()

if max(l) >= 3:
  print('No')
else:
  print('Yes')