X = int(input())
stick_len = [64]
cnt = 0


def divide_stick(stick):
    return stick / 2


while X != sum(stick_len):
    stick = min(stick_len)
    if (min(stick_len) / 2) + sum(stick_len) - stick > X:
        stick_len.remove(stick)
        if stick != 1:
            stick_len.append(divide_stick(stick))
    else:
        stick_len.append(divide_stick(stick))
        stick_len.append(divide_stick(stick))
        stick_len.remove(stick)

print(len(stick_len))
