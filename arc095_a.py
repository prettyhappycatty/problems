N = int(input())
X = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[i] = X[i]

sorted_dic = sorted(dic.items(), key=lambda x:x[1])

#print(sorted_dic)

ans_idx1 = N // 2 - 1 #半分より大きい時
ans_idx2 = N // 2 #半分より小さい時
#print(sorted_dic[ans_idx1], sorted_dic[ans_idx2])

for i in range(N):
    if X[i] < sorted_dic[ans_idx2][1]:
        print(sorted_dic[ans_idx2][1])
    else:
        print(sorted_dic[ans_idx1][1])
