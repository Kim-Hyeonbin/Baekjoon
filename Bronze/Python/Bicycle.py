import sys

a = int(sys.stdin.readline())
x = int(sys.stdin.readline())
b = int(sys.stdin.readline())
y = int(sys.stdin.readline())
T = int(sys.stdin.readline())

option_1 = a + 21 * (T - 30 if T > 30 else 0) * x
option_2 = b + 21 * (T - 45 if T > 45 else 0) * y

print(option_1, option_2)
