A, B, C = map(int, input().split())

c = 1000 // C + 1

for i in range(1, c):
    cc = i*C
    if A <= cc and cc <= B:
        print(cc)
        exit()

print(-1) 
