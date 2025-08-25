import sys

T = int(sys.stdin.readline())
PS = []
for _ in range(T):
    PS.append(sys.stdin.readline().strip())

for line in PS:
    parentheses = []
    isVPS = True
    for parenthesis in line:
        if parenthesis == "(":
            parentheses.append(parenthesis)
        elif parenthesis == ")":
            if len(parentheses) < 1:
                isVPS = False
                break
            else:
                parentheses.pop()

    if len(parentheses) > 0:
        isVPS = False

    print("YES" if isVPS else "NO")
