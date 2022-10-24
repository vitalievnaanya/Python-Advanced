command = input()

import collections

queue = collections.deque()

while command != 'End':
    queue.append(command)
    if command == 'Paid':
        queue.pop()
        for _ in range(len(queue)):
            print(queue.popleft())
    command = input()
print(f'{len(queue)} people remaining.')
