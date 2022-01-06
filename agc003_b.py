N = int(input())
list_dic = []
for i in range(N):
    A = int(input())
    list_dic.append(A)

print(list_dic)

cnt = 0
for i in range(len(list_dic)-1):
    s = list_dic[i] // 2
    list_dic[i] %= 2
    #print("now",list_dic[i],list_dic[i+1])
    v = min(list_dic[i], list_dic[i+1])
    list_dic[i+1] -= v
    cnt += v + s
    #print(i,s,v, "rest", list_dic[i+1])

s = list_dic[N-1] // 2
#print(s)

print(cnt+s)