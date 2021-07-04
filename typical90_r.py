import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

def f(t):
    chokudai_z = float(L)/2 - math.cos(float(t)*2.0*math.pi/float(T))*float(L)/2
    chokudai_y = 0.0 - math.sin(float(t)*2.0*math.pi/float(T))*float(L)/2
    chokudai_x = 0.0
    statue_x = float(X)
    statue_y = float(Y)
    statue_z = 0.0
    #print(chokudai_x,chokudai_y,chokudai_z, statue_x,statue_y,statue_z)
    return theta(statue_x,statue_y,statue_z,chokudai_x,chokudai_y,chokudai_z)

def theta(x,y,z,x1,y1,z1):
    dxy = math.sqrt((y1-y)**2+(x1-x)**2)
    dz = abs(z1-z)
    #print(dx, dz, "dz/dx",dz/dxy)
    return math.atan2(dz,dxy)*180.0/math.pi

for i in range(Q):
    tmpT = int(input())
    print(f(tmpT))
