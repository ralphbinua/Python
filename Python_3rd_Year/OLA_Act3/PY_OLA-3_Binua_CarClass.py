print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer


car1 = Car("Model S", "Tesla", "Red")
car2 = Car("Mustang", "Ford", "Blue")
car3 = Car("Civic", "Honda", "Black")

print("Car 1:", car1.color, car1.model, car1.manufacturer)
print("Car 2:", car2.color, car2.model, car2.manufacturer)
print("Car 3:", car3.color, car3.model, car3.manufacturer)