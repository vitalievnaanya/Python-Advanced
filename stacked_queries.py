queries = int(input())
query = []

while queries > 0:
    command = input().split()

    if command[0] == '1':
        query.append(int(command[1]))
    elif command[0] == '2':
        if query:
            query.pop()
        else:
            queries -= 1
            continue
    elif command[0] == '3':
        if query:
            print(max(query))
    elif command[0] == '4':
        if query:
            print(min(query))
    queries -= 1

reversed_query = []

for _ in range(len(query)):
    reversed_query.append(str(query.pop()))
print(", ".join(reversed_query))
