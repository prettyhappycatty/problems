H, W = list(map(int, input().split()))

print('#'*(W+2))
for i in range(H):
    s = input().split()
    print('#'+''.join(s)+'#')

print('#'*(W+2))
