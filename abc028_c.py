A, B, C, D, E = map(int, input().split())

ary = [A, B, C, D, E]

bi_s = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    if i+j+k+l+m == 3:
                        bi_s.append(i*A+j*B+k*C+l*D+m*E)

bi_s.sort()
#print(bi_s)

print(bi_s[len(bi_s)-3])