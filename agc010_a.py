N = int(input())

dic = {0:0, 1:0}

A = list(map(int, input().split()))

for i in range(N):
    tmp = A[i] % 2
    dic[tmp] += 1

if dic[1] % 2 == 1:
    print("NO")
else:
    print("YES")
#print(dic)