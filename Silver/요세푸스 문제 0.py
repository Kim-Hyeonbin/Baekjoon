N, K = map(int, input().split())

people = [i + 1 for i in range(N)]
res = []

while len(people) > 0:
    for _ in range(K - 1):
        people.append(people[0])
        people[0:] = people[1:]
    res.append(str(people[0]))
    people[0:] = people[1:]

print("<" + ", ".join(res) + ">")
