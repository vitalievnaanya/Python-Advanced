given_string = input().split()

reversed_string = []

for _ in range(len(given_string)):
    reversed_string.append(given_string.pop())
print(' '.join(reversed_string))
