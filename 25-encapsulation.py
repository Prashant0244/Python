class Student:
    def __init__(self):
        self.name = "Nick"
        self._subject = "History"
        self.__marks = 60

    def show(self):
        print(self.name)
        print(self._subject)
        print(self.__marks)


obj = Student()

obj.name = "Nicky"
obj._subject = "Chemistry"
obj.__marks = 40 # Won't change because it is private

obj.show()