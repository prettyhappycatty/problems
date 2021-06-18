N = int(input())

a = N // 11
b = N % 11

s = a * 2
if b > 6:
    s += 2
elif b > 0:
    s +=1

print(s)