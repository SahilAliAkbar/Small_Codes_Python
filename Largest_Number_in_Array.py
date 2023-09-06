heights = [100, 2, 300, 10, 11, 1000]
largest_number = heights[0]
for number in heights:
    if number > largest_number:
        largest_number = number
print(largest_number)