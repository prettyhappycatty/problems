#TLE

N = int(input())
a = list(map(int, input().split()))

dic = {}

for i in range(N):
    if a[i] not in dic.keys():
        dic[a[i]] = 0
    dic[a[i]] += 1

#print(dic)
msum_0 = []
msum_1 = []

for key in dic.keys():
    msum_1.append(int((dic[key]-1)*(dic[key]-2) /2))
    msum_0.append(int(dic[key]*(dic[key]-1) /2))

print(msum_0)
print(msum_1)

for i in range(N): 
    mulsum = 0
    j = 0
    for key, value in enumerate(dic.items()):
        if key == a[i]:
            mulsum += msum_1[key-1]
        else:
            mulsum += msum_0[key-1]
    j += 1
    print(mulsum)
