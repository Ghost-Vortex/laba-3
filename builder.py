class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, {self.topping} topping"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def set_topping(self, topping):
        self.pizza.topping = topping
        return self

    def build(self):
        return self.pizza

if __name__ == "__main__":
    pizza = PizzaBuilder().set_dough("thin").set_sauce("tomato").set_topping("cheese").build()
    print(pizza)
