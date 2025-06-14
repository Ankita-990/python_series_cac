# *args is a tuple that can hold any number of arguments
# we can use other name for the variable, but 'args' is always consider on industry standards
# *args has all iterable operations which tuple can perform

def sum_all(*args):
    for i in args:
        print(i ** 2)
    return sum(args)

# print("Sum =", sum_all(1,2))
# print("Sum =", sum_all(1,2,3,4,5))
print("Sum =", sum_all(1,2,3,4,5,6,7,8,9))