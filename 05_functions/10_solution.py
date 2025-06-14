# Resursice funtion
# - a function which call itself again and again and only stops when certain condition is not met

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print("Factorial =", factorial(12))