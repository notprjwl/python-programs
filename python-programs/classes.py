# class Vehicle:
#     def __init__ (self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# a = Vehicle(100, 30)
# print(a.max_speed, a.mileage)

# class Vehicle:
#     pass


# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# a = Bus('tata', 100, 30)

# print(a.name)

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
# class Bus(Vehicle):
#     # capacity = 50
#     def seating_capacity(self, capacity=50):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
    
#     def __str__(self):
#         return str(self.seating_capacity()) 
        
# a = Bus('tata bus', 100, 30)

# print(a.seating_capacity())

# class Vehicle:
#     color = 'white'
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#         # self.color = color
       
#     def __str__(self):
#         return f'Color: {self.color}, Vehicle name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'
    
#     def change(cls):
#         cls.color = 'red'
#         return cls.change

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# c = Car('benz', 100, 50)
# c.change()
# print(Vehicle.color)
# print(c.color)

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * self.pi * self.radius
      
a = Circle(5)
print(a.area())
print(a.perimeter())
