import sys


# 병합 정렬을 위해 길이가 1이 될 때까지 리스트를 반으로 쪼개는 함수
def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])
    return merge(left, right)


# 크기에 따라 리스트를 병합하는 함수
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # left나 right 중 하나에 남은 마지막 인덱스를 병합
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for n in range(N)]

for n in merge_sort(nums):
    print(n)
