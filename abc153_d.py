import math
H = int(input())

def attack(monster):
    if monster == 1:
        return 1
    else:
        print(monster)
        return 2*attack(monster//2)+1
        

cnt = attack(H)
print(cnt)