import math

path = 'day-1-input.txt'

file = open(path, 'r')

input_array = file.readlines()
input_array = list(map(lambda x : int(x.rstrip()), input_array))

input_array = list(map(lambda fuel: math.floor(fuel/3) - 2, input_array))

part_1_ans = 0
for fuel in input_array:
    part_1_ans+= fuel
print(part_1_ans)