string = input()
parentheses = []

for i, el in enumerate(string):
    if el == '(':
        parentheses.append(int(i))
    elif el == ')':
        start_index = parentheses.pop()
        last_index = i + 1
        print(f'{string[start_index:last_index]}')
