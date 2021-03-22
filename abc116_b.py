s = int(input())

ary = []

def do(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

def check(n, a):
    for i in range(len(a)):
        if a[i] == n:
            return False
    return True

count = 1
n = s
while check(n, ary):
    #print(n, ary)
    ary.append(n)
    n = do(n)
    count += 1

print(count)


