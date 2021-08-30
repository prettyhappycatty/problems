N = int(input())

dic = {}

for i in range(N):
    S, T = input().split()
    if S+"-"+T not in dic.keys():
        dic[S+"-"+T] = 0
    dic[S+"-"+T] += 1

for k in dic.keys():
    if dic[k] > 1:
        print("Yes")
        exit()

print("No")