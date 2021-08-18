N, K = map(int, input().split())
MOD = 10**9 + 7
if K < 3:
    print(0)
    exit()

if K == 3:
    print(K*(K-1))
    exit()

ab_mod_m = []

a = K-2
b = K-2
ab_mod_m.append(1)
ab_mod_m.append(b)

while len(ab_mod_m) < 100000:
    b = (K-2)*b
    a = b % MOD
    ab_mod_m.append(a)
    #print(b)

print(ab_mod_m)


def change10ton(s, n):#sはString
    sumn = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % n)
        tmp2 = tmp // n
        sumn = tmp1 + sumn 
        tmp = tmp2
    return sumn

def getk(s):
    ans = 1
    #print(s)
    for i in range(len(s)):
        #print(i, s, s[i], len(s)-i, len(s))
        #print(ab_mod_m[(len(s)-i)])
        if s[i] == '1':
            ans *= ab_mod_m[(len(s)-i)] % MOD
    return ans

print(ab_mod_m)

#print("N-2",N-2)
s = change10ton(str(N-2), 2)
print(s, len(s))
ans = getk(s)
print(2**11)
ans2 = (615**2019) % MOD
print(ans% MOD, ans2)

print(K*(K-1)*ans % MOD)
