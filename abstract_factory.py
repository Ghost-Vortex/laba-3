class Chair:
    def sit_on(self):
        pass

class ModernChair(Chair):
    def sit_on(self):
        return "Sitting on modern chair"

class VictorianChair(Chair):
    def sit_on(self):
        return "Sitting on victorian chair"

class Sofa:
    def lie_on(self):
        pass

class ModernSofa(Sofa):
    def lie_on(self):
        return "Lying on modern sofa"

class VictorianSofa(Sofa):
    def lie_on(self):
        return "Lying on victorian sofa"

class FurnitureFactory:
    def create_chair(self):
        pass
    def create_sofa(self):
        pass

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return ModernChair()
    def create_sofa(self):
        return ModernSofa()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return VictorianChair()
    def create_sofa(self):
        return VictorianSofa()

if __name__ == "__main__":
    factory = ModernFurnitureFactory()
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    print(chair.sit_on())
    print(sofa.lie_on())
