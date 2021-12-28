N = int(input())

#f(1)=1
#f(2)~f(9)=0
# f(10)=1
# f(11)=2
# f(12)~f(19)=1
# f(20)~f(99)=0
# f(100)~f(109)=1
# f(110) = 2
# f(111) = 3

# 1桁＝合計1
# 2桁＝合計11
# 3桁＝合計111

def getCount(k, n):
    #n未満で先頭にk個つくものを数える
    a = int("1"*k)
    b = int("1"*(k-1)+"2")
    #print(b,a,b-a)
    x = 1
    cnt = 0
    while b*x <= n:
        #print(b*x, a*x, b*x-a*x)
        cnt += b*x-a*x
        x = x*10
    if a*x <= n:
        #print("a",cnt, n-a*x+1, a*x)
        cnt += max(0, n-a*x+1)
    #print(k,cnt)
    return cnt

ans = 0
for i in range(1,16):
    ans += getCount(i, N)
print(ans)



    