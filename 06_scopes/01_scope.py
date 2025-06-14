username = "xyz"

def func():
    username = "abc"
    print(username)
    
# func()
# print(username)


x = 99

def func2(y):
    z = x + y
    return z

result = func2(1)
# print(result)

# def func3():
#     global x    # never use this syntax; not a good practice
#     x = 88
    

# func3()
# print(x)

def f1():
    # x = 88
    def f2():
        print(x)
    return f2       # return reference of a function

myResult = f1()
# myResult()

def chaicoder(num):
    def actual(x):
        return x ** num     
    return actual           # return defination of function

f = chaicoder(2)    # num = 2
g = chaicoder(3)    # num = 3

# x = 5 (in both cases)
print(f(5))             # factory function or clouser
print(g(5))             # factory function or clouser

## Another example of Clouser or Factory function
def c1(a):
    def c2(b):
        def c3(c):
            return (c + b) * a
        return c3
    return c2

res1 = c1(2)        # a = 2
res2 = res1(4)      # b = 4
print(res2(4))      # c = 4