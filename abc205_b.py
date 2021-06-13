N = int(input())

A = list(map(int, input().split()))

dic = {}

for i in range(N):
    if A[i]-1 not in dic.keys():
        dic[A[i]-1] = 1
    else:
        dic[A[i]-1] += 1

#print(dic)

for i in range(N):
    if i not in dic.keys() or dic[i] != 1:
        print("No")
        exit()

print("Yes")