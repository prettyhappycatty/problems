N = int(input())

dic = {}
for i in range(N):
    tmp = input()
    if tmp not in dic.keys():
        dic[tmp] = True
        print(i+1)

    
