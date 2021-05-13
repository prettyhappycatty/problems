N, M = map(int, input().split())

flg = 0
if N == 1 and M == 0:
    flg = -1

dic = {}
for i in range(M):
    tmp_s, tmp_c = map(int, input().split())
    if N == 1 and tmp_s == 1 and tmp_c == 0:
        flg = -1
        break

    if tmp_s == 1 and tmp_c == 0:
        flg = 1
        break
    if tmp_s > N:
        flg = 1
        break

    if tmp_s not in dic.keys():
        dic[tmp_s] = tmp_c
    
    if dic[tmp_s] != tmp_c:
        flg = 1
        break

if flg == 0: #答えがある
    ans_s = ''
    for i in range(1, N+1):
        if i == 1 and i not in dic.keys():
            ans_s += '1'
        elif i != 1 and i not in dic.keys():
            ans_s += '0'
        elif i in dic.keys():
            ans_s += str(dic[i])
    print(ans_s)
elif flg == 1:
    print('-1')
elif flg == -1:
    print('0')
