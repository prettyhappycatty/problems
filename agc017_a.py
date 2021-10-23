N, P = map(int, input().split())

def mod2(e):
    return e % 2

A = list(map(mod2,map(int, input().split())))

#print(A)

dic = {0:0, 1:0}
for i in range(len(A)):
    dic[A[i]] += 1

#print(dic)

if dic[1] == 0: #全部偶数の場合
    if P == 1:
        print(0)
    else: 
        print(2**N)
else:
    print(2**(N-1))