class Parent:
    def cars(self):
        print("car has four wheels")
    def bikes(self):
        print("bikes has 2 wheels")
    def __init__(self, a, b):
        print("This is a default tag line")
        print(a+b)

obj = Parent(2, 3)
obj.cars()
obj.bikes()
