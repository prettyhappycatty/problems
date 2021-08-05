import math

A, B, W = map(int, input().split())

biggest = math.floor(W*1000/A) #全部Aだとしたら何個
smallest = math.ceil(W*1000/B) #全部Bだとしたら何個

if smallest > biggest:
    print("UNSATISFIABLE")
else:
    print(smallest, biggest)