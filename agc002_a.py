a, b = list(map(int, input().split()))

if 0 < a and 0 < b:
    print("Positive")
elif a <= 0 and 0 <= b:
    print("Zero")
else:
    if (b - a) % 2 == 1:
        print("Positive")
    else:
        print("Negative")

