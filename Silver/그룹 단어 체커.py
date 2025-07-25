import sys

N = int(sys.stdin.readline())

words = [sys.stdin.readline().strip() for _ in range(N)]

cnt = 0
for word in words:
    alphabet = []
    for w in range(len(word)):
        if word[w] not in alphabet:
            alphabet.append(word[w])
        else:
            if word[w - 1] != word[w]:
                cnt += 1
                break
print(N - cnt)
