import sys

N = int(sys.stdin.readline())
total_money = 0

for _ in range(N):
    bill = int(sys.stdin.readline().split()[0])

    if bill == 136:
        total_money += 1000
    elif bill == 142:
        total_money += 5000
    elif bill == 148:
        total_money += 10000
    elif bill == 154:
        total_money += 50000
    else:
        continue

print(total_money)
