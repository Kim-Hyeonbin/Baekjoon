import sys

next = 1
stack = []

n = int(sys.stdin.readline())
result = ""

for _ in range(n):
    target = int(sys.stdin.readline())

    while next <= target:
        stack.append(next)
        next += 1
        result += "+"

    if stack[-1] == target:
        del stack[-1]
        result += "-"
    elif stack[-1] > target:
        result = "NO"
        break
    else:
        continue

print("NO" if result == "NO" else "\n".join(result))
