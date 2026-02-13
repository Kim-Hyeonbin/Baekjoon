import sys

N, M = map(int, sys.stdin.readline().split())
pokedex, reverse_pokedex = (
    {},
    {},
)  # 포켓몬 도감 번호와 이름을 저장할 딕셔너리와 그 반대의 딕셔너리

for i in range(1, N + 1):
    pokemon = sys.stdin.readline().strip()
    pokedex[i] = pokemon
    reverse_pokedex[pokemon] = i

for _ in range(M):
    input_data = sys.stdin.readline().strip()

    if input_data.isdigit():
        sys.stdout.write(pokedex.get(int(input_data), "None") + "\n")
    else:
        sys.stdout.write(str(reverse_pokedex.get(input_data, "None")) + "\n")
