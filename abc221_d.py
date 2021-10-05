# 座圧、いもす法

N = int(input())

#A, B = [],[]
sabun_dic = {}
for i in range(N):
    tmpA, tmpB = map(int, input().split())
#    A.append(tmpA)
#    B.append(tmpB)
    if tmpA not in sabun_dic.keys():
        sabun_dic[tmpA] = 0
    if tmpA + tmpB not in sabun_dic.keys():
        sabun_dic[tmpA + tmpB] = 0
    sabun_dic[tmpA] += 1
    sabun_dic[tmpA + tmpB] -= 1

#print(sabun_dic)
sorted_sabun_dic = sorted(sabun_dic.items(), key=lambda x:x[0])
#print(sorted_sabun_dic)

days = [tuple((0,0))]
for i in range(len(sorted_sabun_dic)):
    day = sorted_sabun_dic[i][0]
    sa = sorted_sabun_dic[i][1]
    #print(days, days[-1][1]+sa)
    #X日目までがY人
    days.append(tuple((day, days[-1][1]+sa)))
#print(days)


num = {}
for i in range(1,len(days)):
    tmp_num = days[i-1][1]
    days_long = days[i][0]-days[i-1][0]
    #print("num=",tmp_num, days[i][0]-days[i-1][0], "dayslong=",days_long)
    if tmp_num not in num.keys():
        num[tmp_num] = 0
    num[tmp_num] += days_long
#print(sorted(num.items(), key=lambda x:x[0]))

ans = []
for i in range(1, N+1):
    if i not in num.keys():
        ans.append(0)
    else:
        ans.append(num[i])

print(*ans)