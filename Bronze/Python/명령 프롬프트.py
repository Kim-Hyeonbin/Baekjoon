import sys

N = int(sys.stdin.readline())

file = [sys.stdin.readline().strip() for file_name in range(N)]

res = ""

for i in range(len(file[0])):
    text = file[0][i]
    isSame = True
    for j in range(1, N):
        if file[j][i] != text:
            isSame = False
            break
    if isSame:
        res += text
    else:
        res += "?"

print(res)
