import sys

N = int(sys.stdin.readline())

nums = [int(n) for n in sys.stdin.readline().split()]

prime_number_count = 0

for n in nums:

    isprime = True

    if n == 1:
        continue

    for i in range(2, n):
        if n % i == 0:
            isprime = False

    if isprime:
        prime_number_count += 1

print(prime_number_count)
