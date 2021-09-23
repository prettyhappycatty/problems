a, b = map(int, input().split())

aa = str(a)*b
bb = str(b)*a

ary = [aa, bb]

ary.sort()

print(ary[0])
