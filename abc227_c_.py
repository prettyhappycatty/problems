N = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

lst = prime_factorize(N)

cnt_dic = {}

for i in range(len(lst)):
    if lst[i] not in cnt_dic.keys():
        cnt_dic[lst[i]] = 0
    cnt_dic[lst[i]] += 1

print(cnt_dic)

#type1 = 1*1*なにか
#type2 = 1*なにか*なにか
#type3 = なにか*なにか*なにか

type1_cnt = N
type2_cnt = 
    

