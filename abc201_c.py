S = input()

def check(di, s):
    for i in range(10):
        if s[i] == 'x'and i in di.keys():
            return False
        if s[i] == 'o' and i not in di.keys():
            return False
    return True

        

cnt = 0
for i in range(10000):
    keta = []
    keta.append(i // 1000)
    keta.append(i%1000 // 100)
    keta.append(i%100 // 10 )
    keta.append(i%10 // 1)
    #print(keta)
    dic = {}
    for k in keta:
        if k not in dic.keys():
            dic[k] = 0
        dic[k] += 1
    #print(dic)
    ret = check(dic, S)
    if ret == True:
        cnt += 1
print(cnt)