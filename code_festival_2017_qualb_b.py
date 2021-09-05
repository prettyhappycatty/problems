N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

D_dic = {}
for i in range(N):
    if D[i] not in D_dic.keys():
        D_dic[D[i]] = 0
    D_dic[D[i]] += 1


T_dic = {}
for i in range(M):
    if T[i] not in T_dic.keys():
        T_dic[T[i]] = 0
    T_dic[T[i]] += 1

for key in T_dic.keys():
    if key not in D_dic.keys():
        print("NO")
        exit()
    else:
        if D_dic[key] < T_dic[key]:
            print("NO")

print("YES")