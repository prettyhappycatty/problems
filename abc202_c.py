N = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_dic = {}
b_dic = {}
c_dic = {}

for i in range(N):
    if a[i] not in a_dic.keys():
        a_dic[a[i]] = 0
    if b[i] not in b_dic.keys():
        b_dic[b[i]] = 0
    if c[i] not in c_dic.keys():
        c_dic[c[i]] = 0
    a_dic[a[i]] += 1
    b_dic[b[i]] += 1
    c_dic[c[i]] += 1

cnt = 0
for j in range(N):
    if b[c[j]-1] in a_dic.keys():
        cnt += a_dic[b[c[j]-1]]
        #print(cnt)

print(cnt)