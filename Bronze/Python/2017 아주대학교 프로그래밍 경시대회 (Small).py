import sys

num_participants = int(sys.stdin.readline())
records = [
    list(map(int, sys.stdin.readline().split())) for _ in range(num_participants)
]

score = [records[i][0] for i in range(num_participants)]
winner_result = max(score)
winner_index = score.index(winner_result)
score.remove(winner_result)

if winner_result not in score:
    print(winner_index + 1)
else:

    num_submit = [records[i][1] for i in range(num_participants)]
    winner_result = min(num_submit)
    winner_index = num_submit.index(winner_result)
    num_submit.remove(winner_result)

    if winner_result not in num_submit:
        print(winner_index + 1)
    else:

        upload_time = [records[i][2] for i in range(num_participants)]
        winner_result = min(upload_time)
        winner_index = upload_time.index(winner_result)
        print(winner_index + 1)
