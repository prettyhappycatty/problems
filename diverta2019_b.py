

#r, g, b, n = lstdin.readline().rstrip().split()
r, g, b, n = list(map(int, input().split()))

cnt = 0 
for i in range(n//r+1):
    red = i * r
    for j in range(n//g+1):
        green = j * g
        if n < red + green:
            continue
        elif (n - red - green) % b == 0:
            cnt += 1
print(cnt)