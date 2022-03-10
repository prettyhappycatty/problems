N = int(input())

MOD = 998244353

def get(n):
    if n < 10 :
        return n
    else:
        return n - int((len(str(n))-1)*"9")


def n_keta_kosuu_max(n):
    if n == 1:
        return 9
    else:
        return int(n*"9") - int((n-1)*"9")


keta = len(str(N))
#print("keta",keta)

sum_ = 0
for i in range(1, keta):
    keta_kosuu = n_keta_kosuu_max(i)
    s = keta_kosuu*(keta_kosuu+1)//2
    sum_ += s 
    sum_ %= MOD
    #print(i,s)

#print(get(N))
n_keta_kosuu = get(N)
sum_ += n_keta_kosuu*(n_keta_kosuu+1)//2

print(sum_  % MOD)

