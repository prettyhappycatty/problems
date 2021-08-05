s1 = list(input())
s2 = list(input())

s1_sort = sorted(s1)
s2_sort = sorted(s2, reverse=True)

s = ''.join(s1_sort)
t = ''.join(s2_sort)

if s < t:
    print("Yes")
else:
    print("No")