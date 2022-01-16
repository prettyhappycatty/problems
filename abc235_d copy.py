import sys
sys.setrecursionlimit(10**6)

a, N = map(int, input().split())

x = [1]

def irekae(k):
    if k > 10 and k % 10 > 0:
        return k // 10 + (k % 10)*(len(str(k))-1)*10
    else:
        return -1



def dfs(ary):
    ans = []
    for i in range(len(ary)):
        tmp1 = ary[i]*a
        ans.append(tmp1)
        tmp2 = irekae(ary[i])
        if tmp2 > 0:
            ans.append(tmp2)
        if tmp1 == N or (tmp2 >0 and tmp2 == N):
            return 1, ans
    return -1, ans    


for i in range(100):
    flg, x = dfs(x)
    print(x)
    if flg == 1:
        print(i+1)
        exit()

print(-1)
