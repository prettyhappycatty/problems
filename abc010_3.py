import math
txa, tya, txb, tyb, T, V = map(int, input().split())

n = int(input())

def get_2(gx,gy):
    #print(txa,tya,gx,gy,txb,tyb)
    return math.sqrt((gx-txa)**2+(gy-tya)**2)+math.sqrt((gx-txb)**2+(gy-tyb)**2)


for i in range(n):
    x,y = map(int, input().split())
    dist_2 = get_2(x,y)
    #print(dist_2, T*V)
    if dist_2 <= T*V:
        print("YES")
        exit()
print("NO")