N = int(input())
flag = False

for i in range(N):
    nums = [int(str(i)[n]) for n in range(len(str(i)))]
    if (i + sum(nums)) == N:
        flag = True
        break

if flag:
    print(i)
else:
    print(0)
