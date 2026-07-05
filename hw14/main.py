class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    

v1 = Vector(2, 3)
v2 = Vector(3, 4)

print(v1)
print(v2)
print(v1+v2)


class Book:
    def __init__(self, title, author):
        self.title =title
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):  
            return self.title == other.title and self.author == other.author
        return False


book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  
print(book1 == book3)  



class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        
        if not isinstance(value, str):
            raise TypeError("Brand უნდა იყოს ტექსტური ტიპის (str)!")
        if not value.strip():
            raise ValueError("Brand არ შეიძლება იყოს ცარიელი!")
        self._brand = value.strip()

   
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Model უნდა იყოს ტექსტური ტიპის (str)!")
        if not value.strip():
            raise ValueError("Model არ შეიძლება იყოს ცარიელი!")
        self._model = value.strip()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Year უნდა იყოს მთელი რიცხვი (int)!")
        if value < 1886 or value > 2026:
            raise ValueError("Year უნდა იყოს 1886-დან 2026-მდე დიაპაზონში!")
        self._year = value

    
    def __str__(self):
        return f"Car: {self.brand} {self.model} ({self.year})"
    

   
my_car = Car("  Toyota ", "Camry", 2022)
print(my_car)
print(f"ბრენდი: {my_car.brand}")
my_car.year = 2025
print(f"განახლებული წელი: {my_car.year}")
