import math

path = 'Day 1/day-1-input.txt'


def calculate_fuel_required(fuel: int) -> int:
    ans = fuel // 3 - 2
    return ans if ans > 0 else 0


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
part_2 = list(map(lambda x: int(x.rstrip()), input_array))

part_2_ans = 0
for fuel in part_2:
    fuel_needed = 0
    fuel_counter = fuel
    while fuel_counter > 0:
        fuel_counter = calculate_fuel_required(fuel_counter)
        fuel_needed += fuel_counter
    part_2_ans += fuel_needed

print(part_2_ans)
