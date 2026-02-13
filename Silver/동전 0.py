import sys

N, K = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(N)]
num_of_coins = 0

for coin in coins[::-1]:

    num_of_coins += K // coin
    K %= coin

    if K == 0:
        break


sys.stdout.write(str(num_of_coins))
