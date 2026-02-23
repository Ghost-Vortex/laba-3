class Button:
    pass

class WindowsButton(Button):
    def paint(self):
        print("Windows кнопка")

class MacButton(Button):
    def paint(self):
        print("Mac кнопка")

class GUIFactory:
    def create_button(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

factory = WindowsFactory()
button = factory.create_button()
button.paint()
