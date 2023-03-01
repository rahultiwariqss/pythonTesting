from Parent import Parent


class Child(Parent):
    def Animals(self):
        print("Dog")

    def __init__(self):
        Parent.__init__(self, 2, 10)

obj2 = Child()
obj2.bikes()
obj2.cars()
obj2.Animals()