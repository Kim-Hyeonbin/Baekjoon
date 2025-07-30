import sys

T = int(sys.stdin.readline())

answer = ""
for _ in range(T):
    expr = sys.stdin.readline().strip()
    equal_index = expr.find("=")
    res = eval(expr[:equal_index])
    if res == int(expr[equal_index + 1 :]):
        answer += "correct\n"
    else:
        answer += "wrong answer\n"

print(answer.strip())
