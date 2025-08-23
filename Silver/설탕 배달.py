N = int(input())
five = N // 5
isdivided = True
while (N - five * 5) % 3 != 0:
    if five < 1:
        isdivided = False
        break
    five -= 1

if isdivided:
    print(five + (N - five * 5) // 3)
else:
    print(-1)
