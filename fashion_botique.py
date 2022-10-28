sequence_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

left_rack_capacity = rack_capacity
clothes_stack = sequence_of_clothes[::-1]
needed_racks = 1

while len(sequence_of_clothes) > 0:
    for i in range(len(clothes_stack)):
        if int(clothes_stack[i]) <= left_rack_capacity:
            left_rack_capacity -= int(clothes_stack[i])
            sequence_of_clothes.pop()
        else:
            needed_racks += 1
            left_rack_capacity = rack_capacity
            left_rack_capacity -= int(clothes_stack[i])
            sequence_of_clothes.pop()

print(needed_racks)
