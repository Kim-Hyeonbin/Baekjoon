M, N = map(int, input().split())

for i in range(M, N + 1):
    isprime = True
    if i == 1:
        continue

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isprime = False
            break
    if isprime:
        print(i)
