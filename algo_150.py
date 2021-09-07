b = 0b0011010010

cnt = 0
lst = -1
while b > 0:
    mod = b & 0b1 #下1桁マスク
    #print(cnt, mod)
    if mod == 1:
        #print(cnt)
        lst = cnt
    b = b >> 1 #1ビットシフト
    cnt += 1

print(lst)