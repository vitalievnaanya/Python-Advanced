import collections
quantity_water = int(input())

queue = collections.deque()

command = input()

while command != 'Start':
    queue.appendleft(command)
    command = input()

command = input()

while command != 'End':
    if command.startswith('refill'):
        command = command.split()
        quantity_water += int(command[1])
    elif command.isdigit():
        if quantity_water >= int(command):
            quantity_water -= int(command)
            print(f'{queue.pop()} got water')
        else:
            print(f' {queue.pop()} must wait')

    command = input()

print(f'{quantity_water} liters left')