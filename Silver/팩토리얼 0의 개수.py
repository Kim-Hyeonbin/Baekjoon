import sys, math


N = math.factorial(int(sys.stdin.readline()))
zero_count = 0

for d in str(N)[::-1]:
    if d == "0":
        zero_count += 1
    else:
        break

print(zero_count)
