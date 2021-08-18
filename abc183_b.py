Sx, Sy, Gx, Gy = map(int, input().split())

#Goalのy座標をマイナスに（x軸を鏡として線対象に移動）

#直線の傾きaを求める
a = ( (-Gy) - Sy) / ( Gx - Sx)

# Sy = a * x_dash (Sx, Sy), (Sx, 0),(Sx, x)の三角形（x軸上の辺の長さをx_dash）を考える
# x = Sx + x_dash　

x_dash = -Sy/a
x = x_dash + Sx

print(x)