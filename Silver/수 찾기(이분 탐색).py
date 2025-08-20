import sys


def binary_search(L, target, start, end):
    if start > end:
        print(0)
        return
    mid = (start + end) // 2
    if L[mid] == target:
        print(1)
        return
    elif L[mid] > target:
        binary_search(L, target, start, mid - 1)
    else:
        binary_search(L, target, mid + 1, end)


N = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for i in targets:
    binary_search(nums, i, 0, len(nums) - 1)
