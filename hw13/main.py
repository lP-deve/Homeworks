from datetime import datetime

class Car:
    number_of_cars = 0   

    def __init__(self, brand, model, year):
        self.brand = brand 
        self.model = model
        self.year = year

        Car.number_of_cars += 1 

    def car_info(self):
        return f"{self.brand} {self.model} ({self.year}) - car age is {self.age_of_car()}"
    
    def age_of_car(self):
        current_year = datetime.now().year
        car_age = current_year - self.year
        return f" {car_age} years"
    
    @classmethod
    def total_cars(cls):
        return f"მანქანების მთლიან რაოდენობაა {cls.number_of_cars}"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)  
        self.battery_life = battery_life

    def battery_info(self):
        return f"ელემენტის ხანგრძლივობა შეადგენს {self.battery_life} საათს."


car1 = Car("BMW", "X6", 2024)
car2 = Car("Mercedes", "C-Class", 2020)

print(car1.car_info())          
print(car1.age_of_car())       
print(Car.total_cars())

elcar = ElectricCar("Tesla", "Model S", 2022, 12)
print(elcar.car_info())         
print(elcar.age_of_car())       
print(elcar.battery_info())     
print(ElectricCar.total_cars())