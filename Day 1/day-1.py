import math

path = 'day-1-input.txt'


def calculate_fuel_required(fuel: int) -> int:
    return math.floor(fuel/3) - 2


file = open(path, 'r')

input_array = file.readlines()

# Part 1
part_1 = list(map(lambda x: int(x.rstrip()), input_array))
part_1 = list(map(lambda fuel: calculate_fuel_required(fuel), part_1))

part_1_ans = 0
for fuel in part_1:
    part_1_ans += fuel
print(part_1_ans)

# Part 2
