import sys

strings = []
while True:
    s = sys.stdin.readline().strip()
    if s == "#":
        break
    strings.append(s)

for S in strings:
    cnt = 0
    for s in S:
        if s in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            cnt += 1
    print(cnt)
