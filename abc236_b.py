
N = int(input())
A = list(map(int, input().split()))

dic = {(i+1):0 for i in range(N)}


for i in range(len(A)):
    dic[A[i]] += 1

for key,v in dic.items():
    if v < 4:
        print(key)
        exit()
