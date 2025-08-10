import sys

N = int(sys.stdin.readline())
nums = [int(n) for n in sys.stdin.readline().split()]

print(min(nums), max(nums))
