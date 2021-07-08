import copy
k = 3
#パターンの数え上げ
ret = [[i] for i in range(2)]

print(ret)

def add1n(ary,n):
    ret_addn = []
    for a in ary:
        for i in range(n):
            cp = copy.deepcopy(a)
            cp.append(i)
            ret_addn.append(cp)
    return ret_addn


#ret = mkcase(ret, ret2, 6)
for i in range(k):
    ret = add1n(ret,2)
print(ret)
print(len(ret))
