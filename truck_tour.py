sequence_of_petrol_pumps = int(input())

for attempt in range(sequence_of_petrol_pumps):
    petrol, distance = input().split()
    if int(petrol) >= int(distance):
        break

print(attempt)
