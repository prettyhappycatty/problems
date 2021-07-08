import copy,itertools

N, Q = map(int, input().split())

nar = []

def to_bit(s):
    sum9 = ""
    j = 0
    tmp = int(s)
    bi = []
    cnt = 0
    while tmp > 0:
        tmp1 = str(tmp % 2)
        tmp2 = tmp // 2
        if tmp1 == "0":
            bi.append(cnt)
        sum9 = tmp1 + sum9 
        tmp = tmp2
        cnt += 1
    return sum9, bi #下から何桁目が0でなければいけないか


for i in range(N):
    ar = [1 for i in range(60)] 
    nar.append(ar)

#print(nar)
#ar = [[0,0,0], [0,1,0]....]def add1n(ary,n):

def add1n(ary,n):
    ret_addn = []
    for a in ary:
        for i in range(n):
            cp = copy.deepcopy(a)
            cp.append(i)
            ret_addn.append(cp)
    return ret_addn


def mkcase(k):
    #パターンの数え上げ
    ret = [[i] for i in range(2)]

    for i in range(k-1):
        ret = add1n(ret,2)
    return ret



cnt = [0 for i in range(N)]

for i in range(Q):
    x,y,z,w = map(int, input().split())
    s, bi_ar = to_bit(str(w))
    #print(bi_ar)
    for e in bi_ar:
        #print(x,y,z,e)
        nar[x-1][e] = 0
        cnt[x-1] += 1
        nar[y-1][e] = 0
        cnt[y-1] += 1
        nar[z-1][e] = 0
        cnt[z-1] += 1
print(cnt)

def mkpattern(cntcase, tmpcase1, nari):
    nbri = copy.deepcopy(nari)
    i = 0
    for j in range(nbri):
        while i < cntcase):
            if nbri[j] == 1:
                nbri[j] = tmpcase1[i]
                i += 1
    return nbri

mulmul =1
for i in range(N):
    mul = 1
    aset = []
    a = nar[i][0:len(s)]
    tmpcase = mkcase(cnt[i])
    print(tmpcase)

print(mulmul % (10**9+7))

#print(nar)