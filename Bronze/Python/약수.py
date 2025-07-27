import sys

num_count = int(sys.stdin.readline())
div = [int(num) for num in sys.stdin.readline().split()]
print(min(div) * max(div))
