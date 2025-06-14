# __ - make variable private
# Static method - a method which is accessible by Class but not by its instance
# @staticmethod - Decorators
# @property : prevent class parameters to not override once they have been set in a constructor
# pass : null operation or placeholder
#      : used when statement is required but should not be executed
#      : doesn't provide any functionality
# Multiple inheritance is allowed in python

class Car:
    total_car = 0       # Class variable
    
    ## instead of this
    # brand = None
    # model = None
    
    # use this
    # Constructor in python
    def __init__(self, brand, model):    # self works same as this in Java
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand
    
    def set_brand(self, brand):
        self.__brand = brand
        
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diseal"
    
    @staticmethod
    def general_description():
        return "Car is used for a mean of transport"
    
    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.full_name())
# print(my_tesla.fuel_type())
    
my_car = Car("Toyota", "Corolla")
# print(my_car.__brand)

# my_car.model = "X"
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())


# say_car = input("Enter brand : ")
# my_car.set_brand(say_car)
# print(my_car.get_brand())

Car("Tata", "Safari")

# print(Car.total_car)        # Class variable can be called directly

# print(my_car.general_description())
# print(Car.general_description())

class Battery:
    def battery_info(self):
        return "This is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())