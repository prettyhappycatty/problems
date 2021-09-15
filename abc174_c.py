# 鳩の巣原理、あまりがループする

K = int(input())
a = [0 for _ in range(1000001)]

a[0] = 7 % K
if a[0] == 0:
    print(1)
    exit()
    
for i in range(K):
    a[i+1] = ( a[i]*10 + 7 ) % K
    if a[i+1] == 0:
        print(i+2)
        exit()
print(-1)
#print(a)