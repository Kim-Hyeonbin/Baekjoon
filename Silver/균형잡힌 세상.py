import sys

lines = []
line = ""
while True:
    line = sys.stdin.readline().rstrip()

    if line == ".":
        break

    lines.append(line)

for line in lines:
    brackets = [0]
    isright = True

    for letter in line:

        if letter in ("(", "["):
            brackets.append(letter)

        elif letter == ")":
            if brackets[-1] == "(":
                del brackets[-1]
            else:
                isright = False
                break

        elif letter == "]":
            if brackets[-1] == "[":
                del brackets[-1]
            else:
                isright = False
                break

    if len(brackets) > 1:
        isright = False

    print("yes" if isright else "no")
