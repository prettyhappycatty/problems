N, M = list(map(int, input().split()))#問題数N, 回答数M

dic_ac_flg = [0]*N #waをカウントする
ac = 0
wa = 0

#print(dic_ac_flg)
for i in range(M):#回答数M
    tmp1, tmp2 = input().split()
 #   print(len(dic_ac_flg), int(tmp1)-1, tmp1, tmp2)
    if dic_ac_flg[int(tmp1)-1] == 'ac':#指定した問題はすでにACがでている場合
#        print('skip')
        continue#スキップ

    if tmp2 == 'AC':#ACを初めて出した場合
        ac += 1
        wa += dic_ac_flg[int(tmp1)-1]
        dic_ac_flg[int(tmp1)-1] = 'ac'
    elif tmp2 == 'WA':#ACを出す前にWAの時
        dic_ac_flg[int(tmp1)-1] +=1
    else:
        print('?')
    #other dic_ac_flg[tmp1] != 0: do nothing    
    #print(tmp1, tmp2, dic_ac_flg, dic_cnt_ac, dic_cnt_wa)
print(ac,wa)

#todo
