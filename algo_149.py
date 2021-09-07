b = 0b0100101001

b = b >> 3#３ビットシフト
mod = b & 0b1 #下1桁目マスク

print(mod)