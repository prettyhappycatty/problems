N, K = map(int,input().split())

now_in_warret = K
i=0 #今いる街
stop_flg = 0

supply = {}

for i in range(N):
    tmpA, tmpB = map(int,input().split())
    if tmpA not in supply.keys():
        supply[tmpA] = 0
    supply[tmpA] += tmpB

#print(supply)

sup = list(sorted(supply.items(), key=lambda x:x[0]))
#print(sup)

i = 0
town_no = 0
while i < len(sup):
    #print(town_no, sup[i][0], sup[i][1],"w", now_in_warret)
    #街tmpAまで行けるか？
    if sup[i][0]-town_no <= now_in_warret: #補給がない街かつ移動可能な場合
        #print("can")
        now_in_warret -= sup[i][0]-town_no #町までの運賃をひく
        town_no = sup[i][0] #街tmpAまで移動
        now_in_warret = now_in_warret + sup[i][1] 
        #print(town_no, sup[i][0], sup[i][1],"e", now_in_warret)
        i += 1
        continue
    else:
        #print("stop")
        stop_flg = 1
        town_no = town_no + now_in_warret
        break

if stop_flg == 0:
    print(town_no+now_in_warret)
else:
    print(town_no)
