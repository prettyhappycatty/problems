H, W = map(int, input().split())

a = (H + 1) // 2
b = (W + 1) // 2

if H == 1 or W == 1:
    print(H*W)
else:
    print(a*b)