N = int(input())

#Nが2^xと2^(x+1)の間に入るxを求める
def retyz(x, N):
    y = int(N // (2**(x-1)) )
    z = N - y*(2**(x-1))
    return y, z

x = 0
small = 100000000000000000000
if N == 1:
    print(1)
else:
    while 2**x < N:
        x += 1
        y,z = retyz(x, N)
        if small > x+y+z-1:
            small = x+y+z-1
        #print(x,y,z, small)
    print(small)