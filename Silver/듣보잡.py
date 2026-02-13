import sys

N, M = map(int, sys.stdin.readline().split())
unheard = {sys.stdin.readline().strip() for _ in range(N)}
unseen = {sys.stdin.readline().strip() for _ in range(M)}

unheard_and_unseen = sorted(unheard & unseen)
print(f"{len(unheard_and_unseen)}\n" + "\n".join(unheard_and_unseen))
