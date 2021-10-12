T = int(input())
test_cases =[]


# 3x2+2x2
# 3x2+4x1
# 2x5
# 2x3+4x1
# 4x2 + 2x1

#3は必ず偶数個使う->長さ6にしてしまう
#2,4,6から10を作る->1 2 3で5を作る

def cnt(cnt1, cnt2, cnt3):
    ans = 0
    cnt1_ = cnt1
    cnt2_ = cnt2
    cnt3_ = cnt3
    #2と3で作る
    if cnt2_ > 0 and cnt3_ > 0:
        kosuu = min(cnt2_, cnt3_)
        cnt3_ -= kosuu
        cnt2_ -= kosuu
        ans += kosuu
        #print("3,2->", kosuu, cnt1_, cnt2_, cnt3_)

    #2がないとき3と1で作る
    if cnt3_ > 0 and cnt1_ > 1:
        kosuu = min(cnt1_ // 2, cnt3_)
        cnt3_ -= kosuu
        cnt1_ -= kosuu * 2
        ans += kosuu
        #print("3,1,1->", kosuu, cnt1_, cnt2_, cnt3_)
        
    #3がないとき2と1で作る
    if cnt2_ > 1 and cnt1 > 0:
        kosuu = min(cnt1_, cnt2_//2)
        cnt2_ -= kosuu * 2
        cnt1_ -= kosuu
        ans += kosuu
        #print("2,2,1->", kosuu, cnt1_, cnt2_, cnt3_)

    #3がないとき2と1で作る
    if cnt1_ > 4:
        kosuu = cnt1_ // 5
        cnt1_ -= kosuu * 5
        ans += kosuu
        #print("1,1,1,1,1->", kosuu, cnt1_, cnt2_, cnt3_)

    #3がないとき2と1で作る
    if cnt1_ > 2 and cnt2_ > 0:
        kosuu = min(cnt1_ // 3, cnt2_)
        cnt2_ -= kosuu
        cnt1_ -= kosuu * 3
        ans += kosuu
        #print("1,1,1,1,1->", kosuu, cnt1_, cnt2_, cnt3_)

    return ans
    

for i in range(T):
    tmp = list(map(int, input().split()))
    #print(tmp[0], tmp[2], tmp[1]//2)
    ret = cnt(tmp[0], tmp[2], tmp[1]//2)
    print(ret)