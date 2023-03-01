# class Calculator:
#     def sum(self):
#         print("I am the sum class")
#     def Sub(self):
#         print("I am the sub class")
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print("I will be called automatically")
#
#
#     def addition(self):
#         return self.a + self.b
#
# obj = Calculator(2, 3)
# obj.sum()
# obj.Sub()
# print(obj.addition())
#
# obj2 = Calculator(3, 7)
# print(obj2.addition())
#
# class Cars:
#     a = 100
#     b = "Cars"
#
#     def hatchback(self):
#         print("Swift","wagonr")
#
#     def suv(self, c, d):
#         self.c = c
#         self.d = d
#         print("naxon", "punch")
#         print(self.c+self.d)
#
#     def __init__(self):
#         print("I am the king method or you can call me constructor")
#
# obj = Cars()
# obj.hatchback()
# obj.suv(2, 3)



class Cars:

    def hatchBack(self):
        print("this is hatch back segment cars")
    def suv(self):
        print("this is suv cars")

    def muv(self):
        print("This is muv segment cars")

    def __init__(self, c, d):
        print("please dont look at this method as this is premium segment car you cant affort")
        self.c= c
        self.d =d
        print(c+d)

    def cal(self, a, b):
        print(a+b)
        print(self.c, self.d)

obj = Cars(2 ,5)
obj.suv()
obj.muv()
obj.hatchBack()
obj.cal(2, 3)
obj.cal(3, 5)