numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0

for pos_num in numbers:
    if pos_num > 0:
        count += 1
    
print("Count of positive numbers are", count)