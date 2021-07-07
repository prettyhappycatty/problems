import math

N = int(input())

def check_dic_and_inc(dic, n):
    if n not in dic.keys():
        dic[n] = 0
    dic[n] += 1
    return dic

def prime_factorize(n):
    dic = {}
    a = []
    while n % 2 == 0:
        a.append(2)
        dic = check_dic_and_inc(dic, 2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            dic = check_dic_and_inc(dic, f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
        dic = check_dic_and_inc(dic, n)
    return a, dic

a, dic = prime_factorize(N)
#print(a)
#print(dic)

ar_set = []
for k, v in dic.items():
    ar = [1]
    mul = 1
    for i in range(v):
        mul *= k
        ar.append(mul)
    ar_set.append(ar)
    
#print(ar_set)

def armul(ar, ar2):
    new_ar = []
    #print(ar, ar2)
    for i in range(len(ar)):
        for j in range(len(ar2)):
            new_ar.append(ar[i]*ar2[j])
    return new_ar

ar_1 = [1]
for l in ar_set:
    ar_1 = armul(ar_1, l)
ar_1.sort()
#print(ar_1)

cnt = 0
for i in range(len(ar_1)):
    for j in range(i, len(ar_1)):
        modN = N % (ar_1[i] * ar_1[j])
        k = N // (ar_1[i] * ar_1[j])
        if modN == 0 and k >= ar_1[j]:
#            print(ar_1[i],ar_1[j],k)
            cnt += 1
print(cnt)