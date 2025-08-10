import sys

N = int(sys.stdin.readline())

nums = [int(n) for n in sys.stdin.readline().split()]

prime_number_count = 0

for n in nums:

    if n == 1:
        continue

    isprime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isprime = False
            break

    if isprime:
        prime_number_count += 1

print(prime_number_count)
