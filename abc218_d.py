# 長方形の数　N個のvertexから4つを選ぶ

N = int(input())

# list だと通らない（TLE）
p = set([tuple(input().split()) for _ in range(N)])

print(p)
cnt = 0
for i,j in p:
    for k,l in p:
        if i != k and j != l and (i,l) in p and (k,j) in p:
            cnt += 1

print(cnt // 4)