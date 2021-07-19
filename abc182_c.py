s = input()
ar = []
dic = {0:0, 1:0, 2:0}

for i in range(len(s)):
    a = int(s[i]) % 3
    ar.append(a)
    if a == 0:
        continue
    elif a == 1 and dic[2] > 0:
        dic[2] -= 1 
    elif a == 2 and dic[1] > 0:
        dic[1] -= 1
    else:
        dic[a] += 1

#print(ar)
#print(dic)

cnt = 0
for k, v in dic.items():
    if v > 0:
        cnt += v

if cnt == len(s):
    print(-1)
else:
    print(cnt % 3)