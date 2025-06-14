num = 5

value = 1

for i in range(1, 11):
    if i == 5:
        continue
    else:
        value = num * i
    print(num, '*', i, '=', value)