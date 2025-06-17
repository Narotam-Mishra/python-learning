
class Car:
    total_num_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_num_cars += 1

    def get_brand(self):
        return self.__brand + "!"
    
    def display_full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_car = Car("Toyota", "Corolla")
# print("Car's Brand:", my_car.brand)
# print("Car's Model:", my_car.model)
# print("Car's Full Name:", my_car.display_full_name())

my_new_car = Car("Tata", "Safari")
# print("Car's Brand:", my_new_car.brand)
# print("Car's Model:", my_new_car.model)
# print("Car's Full Name:", my_new_car.display_full_name())

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print("Car's brand:",my_tesla.get_brand())
# print("Car's brand:",my_tesla.__brand)
# print("Car's Full Name:",my_tesla.display_full_name())
# print("Car's Fuel Type:", my_tesla.fuel_type())

safari = Car("Tata", "Safari")
# print("Car's Fuel Type:", safari.fuel_type())

my_c = Car("Tata", "Nexon")
# my_c.model = "City"

# print("Total number of cars:", Car.total_num_cars)
# print("General Description of Car:", my_c.general_description())

# print("General Description of Car:", Car.general_description())

# print("my_c Car's model:", my_c.model)

# print("Is my_tesla instance of Car:", isinstance(my_tesla, Car)) 
# print("Is my_tesla instance of ElectricCar:", isinstance(my_tesla, Car)) 


class Battery:
    def battery_info(self):
        return "this is Car's battery"

class Engine:
    def engine_info(self):
        return "this is Car's engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model B")
print("Tesla Engine info:", my_new_tesla.engine_info())
print("Tesla Battery info:", my_new_tesla.battery_info())