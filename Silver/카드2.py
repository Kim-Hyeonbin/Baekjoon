N = int(input())
queue = [i + 1 for i in range(N)]
front = 0
rear = N


while rear - front > 1:
    front += 1
    queue.append(queue[front])
    front += 1
    rear += 1

print(queue[front])
