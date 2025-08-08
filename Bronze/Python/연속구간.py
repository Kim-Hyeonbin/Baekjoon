import sys

for _ in range(3):
    temp_cnt = 1
    max_cnt = 0
    line = sys.stdin.readline()
    for a in range(8):
        if line[a] == line[a + 1]:
            temp_cnt += 1
        else:
            if temp_cnt > max_cnt:
                max_cnt = temp_cnt
            temp_cnt = 1

    print(max_cnt)
