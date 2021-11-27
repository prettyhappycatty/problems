N = int(input())

ary = []
dic = {}
for i in range(N):
    cnt = {}
    s = list(input())
    s.sort()
    sl = ''.join(s)
    if sl not in dic.keys():
        dic[sl] = 0
    dic[sl] += 1

#print(dic)
ans = 0
for k,v in dic.items():
    if v > 1:
        ans +=  v*(v-1)//2

print(ans)
