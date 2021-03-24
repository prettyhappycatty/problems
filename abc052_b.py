N = int(input())
S = input()

x = 0
m = x
for i in range(N):
    if S[i] == 'I':
        x += 1
    else:
        x -= 1
    #print(x)
    if m < x:
        m = x

print(m)