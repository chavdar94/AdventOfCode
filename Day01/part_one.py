file = 'map.txt'
numbers = []

with open(file) as f:
    content = f.readlines()

for line in content:
    line_nums = [s for s in line if s.isdigit()]
    if len(line_nums) == 1:
        line_nums.append(line_nums[0])
    current_num = line_nums[0] + line_nums[-1]
    numbers.append(int(current_num))

print(sum(numbers))
