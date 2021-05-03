N = int(input())

ary = []

for i in range(N):
    tmp = list(reversed(input()))
    ary.append(''.join(tmp))

#print(ary)

new_ary = sorted(ary)


for i in range(N):
    tmp = list(reversed(new_ary[i]))
    print(''.join(tmp))