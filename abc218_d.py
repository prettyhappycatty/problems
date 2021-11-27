# 長方形の数　N個のvertexから4つを選ぶ

def solve():
    #N = int(input())
    N = 2000
    # list だと通らない（TLE）
    #p = set([tuple((i,i)) for i in range(2000)])
    p = [(i,i) for i in range(2000)]

    start = time.time()
    #print(p)
    cnt = 0
    for i,j in p:
        for k,l in p:
            if i != k and j != l and (i,l) in p and (k,j) in p:
                cnt += 1

    print(cnt // 4)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

import time

if __name__ == '__main__':
    solve()