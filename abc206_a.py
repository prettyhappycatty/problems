import math
N = int(input())

a = math.floor(N*1.08)
if ( a< 206):
    print("Yay!")
elif (a == 206):
    print("so-so")
else:
    print(":(")

