# -> Method Overriding and Duck Typing

class Parent:
    def show(self):
        print("Hello")


class Child(Parent):
    def show(self):
        print("Hi")

obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
