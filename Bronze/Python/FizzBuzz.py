import sys

target = 0

for i in range(3, 0, -1):
    line = sys.stdin.readline()

    if line.strip().isdigit():
        target = int(line) + i
        break

if target % 3 == 0 and target % 5 == 0:
    sys.stdout.write("FizzBuzz")
elif target % 3 == 0:
    sys.stdout.write("Fizz")
elif target % 5 == 0:
    sys.stdout.write("Buzz")
else:
    sys.stdout.write(str(target))
