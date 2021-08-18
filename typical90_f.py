import re

N, K = map(int, input().split())
S = input()

let = ['a','b','c','d','e','f',
    'g','h','i','j','k','l',
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

ary = []
for s in let:
    print(S,s)
    m_ar = [m.span() for m in re.finditer(S, s)]
    print(m_ar)
    tmp_ary = []
    if len(m_ar) > 0:
        ctr = 0
        for idx in m_ar:
            while ctr <= idx:
                tmp_ary.append(idx)
                ctr += 1
        while ctr < len(S):
            tmp_ary.append(-1)
            ctr += 1
        ary.append(tmp_ary)
    else:
        tmp_ary = [-1]*N
        ary.append(tmp_ary)
        

print(ary)


print(let)