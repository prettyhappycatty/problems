a, N = map(int, input().split())

x = [N]

def irekae_2(k):
    keta = len(str(k))
    #kの2桁目がゼロでない
    if len(str(k % (10**(keta-1)))) == keta-1:
        #print(keta, k//(10**(keta-1)), k % (10**(keta-1))*10)
        return k//(10**(keta-1)) + k % (10**(keta-1))*10
    else:
        return -1


def dfs(ary):
    ans = set()
    for i in range(len(ary)):
        tmp1 = -1
        if ary[i] % a == 0:
            tmp1 = ary[i] // a
            ans.add(tmp1)

        tmp2 = irekae_2(ary[i])
        if tmp2 > 0:
            ans.add(tmp2)
        if tmp1 == 1 or tmp2 == 1:
            #print(ary)
            #print(ary[i])
            return 1, list(ans)
    return -1, list(ans)    


for i in range(10**4):
    flg, x = dfs(x)
    #print(x)
    if flg == 1:
        print(i+1)
        exit()
    if len(x) == 0:
        print(-1)
        exit()

print(-1)
