import sys


# 병합정렬 알고리즘 구현 연습
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


N = int(sys.stdin.readline())
times = merge_sort(list(map(int, sys.stdin.readline().split())))

total = 0
result = 0

for time in times:
    total += time
    result += total

print(result)
