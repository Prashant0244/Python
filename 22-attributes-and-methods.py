class Animal:
    name = "lion"  # class attribute

    def __init__(self, age):
        self.age = age  # instance attribute

    def show(self):  # instance method
        print(f"I am created using instance method -> {self}")

    @classmethod
    def hello(cls):
        print(f"Hi! I'm created using class method -> {cls.name}")

    @staticmethod
    def static():
        print("Hello! I am created using static method")


obj = Animal(12)

obj.show()
obj.hello()
obj.static()
