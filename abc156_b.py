N, K = map(int, input().split())

# K進法表記から10進法表記にする

def change10ton(s,n):#sはString
    sum9 = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % n)
        tmp2 = tmp // n
        sum9 = tmp1 + sum9 
        tmp = tmp2
    return sum9

print(len(str(change10ton(N,K))))
