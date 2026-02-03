import sys

L = int(sys.stdin.readline())
str = sys.stdin.readline()
result = 0

for i in range(L):
    result += (ord(str[i]) - 96) * 31**i

print(result % 1234567891)
