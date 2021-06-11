N = int(input())

ans = 0
for i in range(1, N+1):
    if str(i).find("7") > -1:
    #    print(str(i))
        continue
    if oct(i).find("7") > -1:
    #    print(oct(i))
        continue
    #print("pass", i)
    ans += 1

print(ans)