m,n,N = list(map(int, input().split()))

bef = N
unused = 0

def recicle(m, n, bef):
    new_num = bef // m
    new_sale = new_num*n
    rest = bef - new_num*m
    #print(new_sale, new_num)
    return rest, new_sale

unused = N
cnt = N

while unused >= m:
    rest, new_sale = recicle(m,n,unused)
    unused = rest + new_sale
    #print('mnunused', m, n, unused, new_sale)
    cnt += new_sale

print(cnt)

