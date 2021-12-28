N = int(input())
S = input()

wa_list = [0] #東を向いている人-西を向いている人
wa = 0
for i in range(N):
    if S[i] == "W":
        wa += 1
    wa_list.append(wa)

#print(wa_list)

min_cnt = N
for i in range(0,N):
    #i番目より左にいて、左を向いている人数
    #i番目より右にいて、右を向いている人数
    #print("リーダーより左",i, "左にいて左を向いてる",wa_list[i]-wa_list[0],"リーダーより右にいる人",N-(i+1), "右にいて左を向いてる",wa_list[N]-wa_list[i+1])
    min_cnt = min(min_cnt,(wa_list[i]-wa_list[0])+(N-(i+1)-(wa_list[N]-wa_list[i+1])))

print(min_cnt)

