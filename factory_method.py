class Car:
    def drive(self):
        pass

class Tesla(Car):
    def drive(self):
        print("Еду на Tesla")

class BMW(Car):
    def drive(self):
        print("Еду на BMW")

class CarFactory:
    def create_car(self, type_):
        if type_ == "tesla":
            return Tesla()
        elif type_ == "bmw":
            return BMW()

factory = CarFactory()
car = factory.create_car("tesla")
car.drive()
