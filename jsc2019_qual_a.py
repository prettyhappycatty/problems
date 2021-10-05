M, D = map(int, input().split())


cnt = 0
for i in range(1, M+1):
    for j in range(10, D+1):
        dd = str(j)
        if int(dd[0])*int(dd[1]) == i and int(dd[0])>1 and int(dd[1])>1:
            cnt += 1

print(cnt)