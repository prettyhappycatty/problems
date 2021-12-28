N = int(input())
A = list(map(int, input().split()))

dic = {}
for i in range(N):
    if A[i] not in dic.keys():
        dic[A[i]] = 0
    dic[A[i]] += 1

#print(dic)

sorted_dic = list(sorted(dic.items(), key=lambda x:x[0], reverse=True))

longer2 = [0,0,0]
longer_cnt = 0
square = -1
for i in range(len(sorted_dic)):
    ll = sorted_dic[i]
    if ll[1] >= 4:
        longer2[longer_cnt] = ll[0]
        longer2[longer_cnt+1] = ll[0]
        longer_cnt += 2
    elif ll[1] > 1: #2本以上ある時
        longer2[longer_cnt] = ll[0]
        longer_cnt += 1

    if longer_cnt >= 2:
        #print(square, longer2[0]*longer2[1])
        square = max(longer2[0]*longer2[1], square)
        print(square)
        exit()

print(0)