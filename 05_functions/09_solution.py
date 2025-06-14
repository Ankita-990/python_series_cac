def generate_number(limit):
    for i in range(2, limit+1, 2):
        yield i
    
for num in generate_number(20):
    print(num)
    
    
# yield returns the value and also remeber the previous state in memory