A, B, C, K = map(int, input().split())
#A, B, Cの順に拾ってく

p2, p3 = 0, 0
if K > A:#Kの枚数より少ない時
    p1 = A
    rest = K - p1
    if rest > B:#K-Aの枚数よりBが少ない時
        p2 = B
        rest = rest - p2
        if rest > C:
            p3 = C
        else:
            p3 = rest
    else:
        p2 = rest
        rest = rest - p2
else:
    p1 = K #全部K

#print(p1, p2, p3)
print(p1-p3)
    


  