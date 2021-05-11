N = int(input())
a = list(map(int, input().split()))

dic = {}

for i in range(N):
    if a[i] not in dic.keys():
        dic[a[i]] = 0
    dic[a[i]] += 1

#print(dic)
mul_all = 0
for key in dic.keys():
    mul_all += dic[key]*(dic[key]-1)/2


for i in range(N): 
    minus = dic[a[i]]*(dic[a[i]]-1)/2
    plus = (dic[a[i]]-2)*(dic[a[i]]-1)/2
    tmp_mull =  mul_all + plus - minus
    print(int(tmp_mull))