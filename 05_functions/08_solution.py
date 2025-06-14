# **kwargs : key-value pair
# can also have more values rather than this key and value pair

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print()
        
print_kwargs(name="dog", sound="bark")
print_kwargs(animal="bat")
print_kwargs(animal="cat", sound="meow", hobby="licking palms")