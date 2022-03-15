from queue import PriorityQueue

n, m = list(map(int, input().split()))
tasks = list(map(int, input().split()))
p_queue = PriorityQueue()
results = [-1] * m
for index in range(len(tasks)):
    if index < n:
        if index >= m:
            break
        p_queue.put((tasks[index], index))
        print(index, 0)
    else:
        time, proc = p_queue.get()
        print(proc, time)
        p_queue.put((time + tasks[index], proc))
