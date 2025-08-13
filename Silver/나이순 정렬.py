import sys


def age_merge_sort(L):

    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = age_merge_sort(L[:mid])
    right = age_merge_sort(L[mid:])

    return merge(left, right)


def merge(left, right):

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if int(left[i][0]) <= int(right[j][0]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


N = int(sys.stdin.readline())
user = []
for _ in range(N):
    user.append(tuple(sys.stdin.readline().split()))

res = age_merge_sort(user)


for n in range(N):
    print(f"{res[n][0]} {res[n][1]}")
