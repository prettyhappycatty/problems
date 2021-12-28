#セグメント木
#https://qiita.com/R_olldIce/items/32cbf5bc3ffb2f84a898

class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length() # 2^(_log) >= n となる最小の整数
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            # 葉に対象の列を格納
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            # 葉に近い場所から順に更新
            for i in range(self._size - 1, 0, -1):
                self._update(i)

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def set(self, p, x):
        assert 0 <= p < self._n
        # 葉に移動
        p += self._size

        self._d[p] = x
        # 関連する場所を更新
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        # 左の結果、右の結果
        sml, smr = self._e(), self._e()

        l += self._size
        r += self._size

        # 未計算の区間がなくなるまで
        while l < r:
            # 自身が右子ノードなら使用
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            # 親に移動
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

#使い方
# def op(結合律の成り立つ演算)　def e(単位元)を定義する
def op(a,b):
    return a + b

def e():
    return 0

segtree = SegTree(op,e,100)
