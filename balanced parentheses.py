parentheses = input()
balanced = True
stack = []

for el in parentheses:
    if el in '([{':
        stack.append(el)
    else:
        last_opening_bracket = stack.pop()
        pair = f'{last_opening_bracket}{el}'
        if pair not in '(){}[]':
            balanced = False
            break
if balanced:
    print(f'YES')
else:
    print(f'NO')
