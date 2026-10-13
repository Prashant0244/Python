# # -> Inheritance

# class Factory:
#     a = "I am a class attribute mentioned inside Factory"

#     def hello(self):
#         print("Hello I am a instance method mentioned inside Factory")


# class FactoryMumbai(Factory):
#     pass


# obj = FactoryMumbai()

# print(obj.a)
# print(obj.hello())


# -> Constructor in Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Hello! {self.name}")


# class Human(Animal):
#     pass


# animal = Animal("lion")

# person = Human("Man")

# animal.show()
# person.show()


# class Laptop:
#     def __init__(self, brand):
#         self.brand = brand

#     def show(self):
#         print(f"This is {self.brand} Laptop")


# class OS(Laptop):
#     def __init__(self, brand, os):
#         super().__init__(brand)
#         self.os = os

#     def show(self):
#         print(f"Laptop -> {self.brand}, OS -> {self.os}")


# obj = Laptop("Asus")
# obj2 = OS("Macbook", "macos")

# obj.show()
# obj2.show()


# -> Multiple Inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Robot(Human, Animal):
#     name3 = 'robot'

# obj = Robot()


# -> Multilevel Inheritance

class MainFactory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips


class BhopalFactory(MainFactory):
    def __init__(self, material, zips, colour):
        super().__init__(material, zips)
        self.colour = colour


class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, colour, pockets):
        super().__init__(material, zips, colour)
        self.pockets = pockets


obj = PuneFactory("Cotton", 3, "Black", 2)

print(obj.pockets)
