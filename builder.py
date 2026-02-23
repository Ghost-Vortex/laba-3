class Computer:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Компьютер состоит из:", ", ".join(self.parts))

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self):
        self.computer.add("CPU")

    def add_gpu(self):
        self.computer.add("GPU")

    def get_result(self):
        return self.computer

builder = ComputerBuilder()
builder.add_cpu()
builder.add_gpu()

pc = builder.get_result()
pc.show()
