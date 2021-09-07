S = 0b00110

S = S >> 2 #1ビットシフト
mod = S & 0b1 #下1桁マスク

if mod == 1:
	print("Yes")
else:
	print("No")