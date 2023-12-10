import re

def extract_numbers(input_string):
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    output = []

    for start_letter in range(len(input_string)):
        for next_letter in range(start_letter, len(input_string) + 1):
            current_word = input_string[start_letter:next_letter]
            if current_word in word_to_number.keys():
                output.append(word_to_number[current_word])
            
        if input_string[start_letter].isdigit():
            output.append(str(input_string[start_letter]))
    return output

file = 'map.txt'
numbers = []

with open(file) as f:
    content = f.readlines()

for line in content:
    nums = extract_numbers(line)
    if len(nums) == 1:
        nums.append(nums[0])

    num = nums[0] + nums[-1]
    numbers.append(int(num))

print(sum(numbers))