N = int(input())

dic = {i:0 for i in range(N)}
for i in range(N-1):
    a,b = map(int, input().split())
    dic[a-1] += 1
    dic[b-1] += 1

for k,v in list(dic.items()):
    if v == N -1:
        print("Yes")
        exit()

print("No")
    
