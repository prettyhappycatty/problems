
n, k = 5, 3
T = [8,1,7,3,9]

#最大積載量p、k台のトラックで積める個数
def kosuu(p):
    i = 0
    j = 0
    while j < k:
        s = 0
        while s + T[i] <= p:
            print(T[i])
            s += T[i]
            i += 1
            if i == n:
                return n
        j += 1
    print(i)
    return i

def solve():#二分探索
    left = 0
    right = 100000 * 100000 #荷物の個数x最大重量
    while right-left >1:
        mid = (right+left)//2
        print('p=',mid)
        v = kosuu(mid) # 2分した真ん中の積載量を出す
        print(right,left,mid)
        if v >= n:
            print(v,'>=',n)
            right = mid
        else:
            left = mid

    return right

ans = solve()

print(ans)
