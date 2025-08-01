nums = list(map(int, input().split()))
div = 1
while True:
    cnt = 0
    for num in nums:
        if div % num == 0:
            cnt += 1
    if cnt >= 3:
        print(div)
        break
    div += 1
