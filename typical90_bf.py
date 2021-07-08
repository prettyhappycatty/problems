N, K = map(int, input().split())

vis = [-1 for _ in range(100000)]

def str_to_wa(s):
    cnt = 0
    for i in range(len(s)):
        #print(s[i])
        cnt += int(s[i])
    a = cnt+int(s)
    return a % 100000

#print(vis)
x = N
cnt = 0
dic = {}
while True:
    tmp_x = x
    x = str_to_wa(str(x))
    #print(x)
    if cnt == K-1:
        print(x)
        exit()

    if x in dic.keys():
        #tmp = x
        v = vis[x]
        cicle_a = cnt - vis[x]
        cicle_b = vis[x]
        dic[tmp_x] = x
        vis[x] = cnt
        break
    vis[x] = cnt
    dic[tmp_x] = x
    cnt += 1
#print(dic)
#print(tmp, "loops_idx", v, "loope_idx",cnt, cicle_a)

if cicle_a < 2:
    print(x)
    exit()

K = (K - cicle_b) % cicle_a

#この条件を通るとき
if K-2 < 0:
    K = K + cicle_a


#print(cnt-v-1, K, (K-v) )
#K = (K-v) % (cnt-v-1)

#print(dic)
cnt = 0
#x = tmp
while True:
    x = dic[x]
    #x = x
    #print(x)
    if cnt == K-2:
        print(x)
        exit()
    cnt += 1
    