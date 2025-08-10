import sys

N, M = map(int, sys.stdin.readline().split())
cards = [int(n) for n in sys.stdin.readline().split()]

max_of_sum = 0

for c_1 in cards:
    for c_2 in cards:
        if c_1 == c_2:
            continue
        for c_3 in cards:
            if (c_1 == c_3) or (c_2 == c_3):
                continue

            sum_of_cards = c_1 + c_2 + c_3

            if sum_of_cards <= M and sum_of_cards > max_of_sum:
                max_of_sum = sum_of_cards


print(max_of_sum)
