# K進法表記から10進法表記にする

def changekto10(k, s):#sはString
    sumk = 0
    j = 0
    for i in range(len(s)-1, -1, -1):
        sumk += int(s[i])*(k**j)
        j += 1
    return sumk

K = int(input())
A, B = map(int, input().split())

print(changekto10(K, str(A))*changekto10(K, str(B)))