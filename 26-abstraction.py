from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def parameter(self):
        pass

    @abstractmethod
    def diameter(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side = side

    def parameter(self):
        print('parameter')

    def diameter(self):
        print('diameter')

class Circle():
    def __init__(self,radius):
        self.radius = radius

    def parameter(self):
            print('parameter')
    
    def diameter(self):
        print('diameter')

obj = Square(12)