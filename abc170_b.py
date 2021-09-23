X, Y = map(int, input().split())

for i in range(101):
    for j in range(101):
        if i+j == X and i*2 + j*4 == Y:
            print("Yes")
            exit()
print("No")