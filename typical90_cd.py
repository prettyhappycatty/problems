L, R = map(int,input().split())


cnt = 0

lenL = len(str(L))
lenR = len(str(R))


def sumAtoB(a,b):
    return (a+b)*(b-a+1)//2

if lenL == lenR:
    cnt = 0
    cnt += sumAtoB(L,R)*lenL
    print(cnt % (10**9+7))
    exit()

if lenR - lenL == 1:
    #次の桁までの個数
    cnt =0
    cnt += sumAtoB(L,10**lenL-1)*lenL
    cnt += sumAtoB(10**lenL,R)*lenR
    print(cnt % (10**9+7))
    exit()

cnt = 0
for i in range(lenL, lenR+1):
    if i == lenL:
        #次の桁までの個数
        #print(L,10**lenL-1,lenL)
        cnt += sumAtoB(L,10**lenL-1)*lenL % (10**9+7)
    elif i == lenR:
        #前の桁までの個数
        #print(10**(lenR-1),R, lenR)
        cnt += sumAtoB(10**(lenR-1),R)*lenR % (10**9+7)
    else:
        #print(10**(i-1),10**i-1,sumAtoB(10**(i-1),10**i-1)*i,i)
        cnt += sumAtoB(10**(i-1),10**i-1)*i % (10**9+7)

print(cnt % (10**9+7))
