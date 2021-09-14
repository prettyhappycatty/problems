N = int(input())

if N % 1000 == 0:
    print(0)
else:
    print(-(N % 1000 - 1000))