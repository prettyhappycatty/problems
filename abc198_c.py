import math

R, X, Y = list(map(int, input().split()))

def get_dist(x, y):
    return math.sqrt(x**2 + y**2)

dist = get_dist(X, Y)
feet = dist // R
m = dist % R
#print(feet, dist)
if feet == 0 and feet != dist / R:
    feet = 2
elif feet > 0 and feet != dist / R:
    feet += 1
#else: #ぴったりの時

print(int(feet))
