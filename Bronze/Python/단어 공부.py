word = input().upper()
alphabet = {e: 0 for e in set(word)}

if len(alphabet) > 1:
    for w in word:
        alphabet[w] += 1

    result = sorted(alphabet.items(), key=lambda item: item[1], reverse=True)
    print(result[0][0] if result[0][1] > result[1][1] else "?")
else:
    print(list(set(word))[0])
