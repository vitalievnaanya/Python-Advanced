
food_quantity = int(input())
orders = input().split()
restaurant_queue =[]

orders_as_nums = [int(x) for x in orders]
print(max(orders_as_nums))

for _ in range(len(orders_as_nums)):
    restaurant_queue.append(orders.pop())

for order in orders_as_nums:
    if order <= food_quantity:
        food_quantity -= order
        restaurant_queue.pop()
    else:
        break

if len(restaurant_queue) == 0:
    print(f'Orders complete')
else:
    reversed_queue = []
    for _ in range(len(restaurant_queue)):
        reversed_queue.append(restaurant_queue.pop())
    print(f"Orders left: {' '.join(reversed_queue)}")