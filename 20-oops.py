class Car:
    brand = "Toyota"  # attribute

    def hello(self):  # method
        print("Hello!!!")

    print("Hi! I am getting initialized")


# print(Car().brand)
# Car().hello()

obj = Car()  # object

print(obj.brand) # accessing attribute through object
obj.hello() # accessing method through object
