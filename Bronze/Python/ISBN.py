MAX = 99999
ISBN = input()
total = 0
error_index = MAX

for index, number in enumerate(ISBN):

    if number == "*":
        error_index = index
        continue

    if index % 2 == 0:
        total += int(number)
    else:
        total += 3 * int(number)

for i in range(10):
    if error_index % 2 == 0:
        total += i
    else:
        total += 3 * i

    if total % 10 == 0:
        error_number = i
        break
    else:
        if error_index % 2 == 0:
            total -= i
        else:
            total -= 3 * i

print(error_number)
