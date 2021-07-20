s = input()
ar = []
dic = {0:0,1:0, 2:0}

all_cnt = 0
for i in range(len(s)):
    a = int(s[i]) % 3
    all_cnt += a
    all_cnt %= 3
    ar.append(a)
    dic[a] += 1

#print(all_cnt)
#print(ar)
#print(dic)

if all_cnt == 0:
    print(0)
elif all_cnt == 1:
    if dic[1] > 0 and len(s) != 1:#1を取り除く場合
        print(1)
    elif dic[2] > 1 and len(s) != 2:#2を2個取り除く場合
        print(2)
    else:
        print(-1)
else:#2余る場合
    if dic[2] > 0 and len(s) != 1:#2を1個取り除く場合
        print(1)
    elif dic[1] > 1 and len(s) != 2:#1を2個取り除く場合
        print(2)
    else:
        print(-1)