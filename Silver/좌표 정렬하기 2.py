import sys

N = int(sys.stdin.readline())


def coordinate_merge_sort(L):

    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = coordinate_merge_sort(L[:mid])
    right = coordinate_merge_sort(L[mid:])

    return merge_coordinate(left, right)


def merge_coordinate(left, right):

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            merged.append(left[i])
            i += 1
        elif left[i][1] > right[j][1]:
            merged.append(right[j])
            j += 1
        else:
            if left[i][0] < right[j][0]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

merged_coordinates = coordinate_merge_sort(coordinates)

for i in merged_coordinates:
    print(f"{i[0]} {i[1]}")
