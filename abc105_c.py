import sys
sys.setrecursionlimit()

N = int(input())

if N == 0:
    print(N)
    exit()

#4で割ったあまり（下2桁の並び）
waru4= ["00", "01", "10", "11"]


ans_str = ""
shou = N
    #print(n)
while abs(shou) > 0:
    amari = (shou % 4 + 4) % 4
    shou = (shou + (shou % 4))// 4
    ans_str =  waru4[amari] + ans_str

    #print("amari,shou=", amari, shou)
print(int(ans_str))