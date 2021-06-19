class Car:
    def __init__(self, brand, type):
        self.brand = brand
        self.type = type

    def run(self):
        self.speed = 10
        return self


car = Car("W", "e")

c1 = car.run()

print (c1.speed)



