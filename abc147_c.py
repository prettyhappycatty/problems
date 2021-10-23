N = int(input())

import itertools

lst = list(itertools.product([0,1], repeat=(N)))


A = []
for i in range(N):
    tmpA = int(input())
    xy_list = []
    for j in range(tmpA):
        x, y = map(int, input().split())
        xy_list.append(tuple((x,y)))
    A.append(xy_list)

#print(A)   

cnt_max = 0
#print(lst)
for l in range(len(lst)):
    ll = lst[l]
    #print(ll)
    flg = False
    #print(xy_list[j][0])
    cnt = 0
    for i in range(N): #A[i]について回す
        xy_list = A[i]#一人目の証言
        #print(i,xy_list)
        if flg:
            continue
        
        if ll[i] == 0:#本人が嘘つきの場合次ループへ
            continue #次のループへ
        elif ll[i] == 1:#正直者の場合カウントする
            cnt += 1

        for k in range(len(xy_list)): #A[i]の証言について回す
            if flg:
                continue
            who = xy_list[k][0]-1
            is_honest = xy_list[k][1]
            #print("(who, honest,k,ll[who])",who, is_honest,ll[who])
            #print(who, "は", is_honest,)


            if is_honest != ll[who]:#bit設定と、矛盾するかどうか
                #print(who,is_honest,ll,":矛盾")
                flg = True

    if flg == False:#矛盾がない場合                    
        cnt_max = max(cnt, cnt_max)

print(cnt_max)

