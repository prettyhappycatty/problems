N = int(input())
A = list(map(int, input().split()))

A_map = {}

def intTotf(i):
    ret = []
    j = 8
    cnt = 0
    while j >= 0:
        bi = (i+1) // (2**j)
        rest = (i+1) % (2**j) #あまり部分
        print(i, j, bi, rest)
        if bi == 1:
            print(A[j-1])
            ret.append(A[j-1])
            cnt += A[j-1]
            cnt = cnt % 200
            print(cnt)
        j -= 1
    return ret, cnt
        

mod_map = {}
flg = 0
for i in range(2**8):
    ary, m = intTotf(i)
    print(ary, m)
    if m not in mod_map.keys():
        mod_map[m] = ary
    else:
        print("Yes")
        print(mod_map[m])
        print(ary)
        flg = 1
        break

if flg == 0:
    print("No")


        