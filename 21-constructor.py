class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"your object details are {self.material}, {self.zips}, {self.pockets}")


reebok = Factory("leather", 3, 2)

campus = Factory("nylon", 3, 3)

# print(reebok.pockets)
# print(campus.pockets)

reebok.show()
