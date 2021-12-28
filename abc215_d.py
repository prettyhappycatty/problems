
def prime_factorize(n): #素因数を配列で返す関数
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
    
def eratosthenes(flist):#エラトステネスのふるいをベース
    #Mは引数じゃなくてそのまま使う
    ret = [i for i in range(1, M+1)] #sqrtまでじゃなくてMまで回す
    for i in range(1, M):
        #print(ret[i], ret[i] in flist.keys())
        if ret[i] > 0 and ret[i] in flist.keys(): #渡された素因数にあるときに除去する
            j = ret[i]
            while 1:
                #倍数を除去
                j += ret[i]
                if j-1 >= M:
                    break
                ret[j-1] = -1
            ret[i] = -1

    #ret[0] = -1 #1を素数から除く部分はコメントアウト
    #残ったものを返すために配列を作る
    ret2 = []
    for i in range(len(ret)): 
        if ret[i] > 0:
            ret2.append(ret[i])
    return ret2 



#main
N, M = map(int,input().split())
A = list(map(int, input().split()))

#Aを素因数のディクショナリ（重複を削除するため、アクセスを簡単にするため）にする
A_fct = {}
for i in range(len(A)):
    fact = prime_factorize(A[i])
    for j in range(len(fact)):
        A_fct[fact[j]] = True

#素因数のディクショナリを渡してエラトステネスの古いっぽいことをする
lst = eratosthenes(A_fct)

print(len(lst))
for i in range(len(lst)):
    print(lst[i])
