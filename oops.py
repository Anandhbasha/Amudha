# #OOps
# carMilage = 18
# carseat = 5
# airbags=5
# wheels = 4
# mirror = 3 

# def brake():
#     print("Car Stops")
# def acc():
#     print("Car Moving")

# carMilage1 = 20
# carseat1 = 8
# airbags1=5
# wheels1 = 4
# mirror1 = 3 

# def brake1():
#     print("Car Stops")
# def acc1():
#     print("Car Moving")


# OOP
# class

# class Cars:
#     carName = "Tata_nexon"
#     No_of_wheels = 4
#     airbags = 5
#     milage = 18
#     mirror = 3
#     def brake1(self):
#         print(f'{self.carName} Stopped')
#     def acc1(self):
#         print(f"{self.carName} Moving")
# # Object
# car1 = Cars()
# car1.milage = 20
# car1.carName="Tata_indico"
# print(car1.milage)
# car1.brake1()
# car1.acc1()

# car2 = Cars()
# car2.brake1()
# car2.acc1()


# # private
# __names = "xyz"
# # protect
# _news = "hg"
# public

# # encapsulation
# class BankAccount:
#     __balance = 0
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f'Amount {amount} Credited')
#         else:
#             print("Invalid Amount")
#     def withdraw(self,amount):
#         if 0 < amount <= self.__balance:
#             self.__balance-=amount
#             print(f'Amount {amount} Debited')
#         else:
#             print("Insufficient Amount")
#     def showBalance(self):
#         return self.__balance

# acc1 = BankAccount()
# acc1.deposit(1000)
# acc1.withdraw(500)
# print(acc1.showBalance())


# list = [11,22,33]
# [2,4,6]

# Inheritence
# class vehicle:
#     def brake(self):
#         print("Vehicle stops")
# class bike(vehicle):
#     def acc(self):
#         print("Bike moves")
# class car(bike):
#     def prints(self):
#         print("car moving")


# # v = bike()
# # v.brake()
# # v.acc()

# c= car()
# c.brake()
# c.acc()


# polymorphism //multiple forms
# # overriding
# class Restuarant:
#     def placeOrder(self):
#         print("Order placed from Genral Restaurant")
# class VegRes(Restuarant):
#     def placeOrder(self):
#         print("Order placed from Veg Restaurant")
# class NVRes(Restuarant):
#     def placeOrder(self):
#         print("Order placed from Non-Veg Restaurant")

# r = Restuarant() #create instence or object creation
# vr = VegRes()
# nv = NVRes()
# r.placeOrder()
# vr.placeOrder()
# nv.placeOrder()
# overloading
# class calculator:
#     def add(self,*a):
#         if len(a)==3:
#             return a[0]+a[1]+a[2]
#     def add(self,*a):
#         if len(a)==2:
#             return a[0]+a[1]
#     def add(self,a):
#         return a
#     def add(self):
#         print("Calc is working")

# calc = calculator()
# print(calc.add(20,30,40))
# print(calc.add(20,30))
# print(calc.add(20))
# calc.add()


# overloading
class calc:
    def add(self,a=0,b=0,c=0):
        return a+b+c

cal = calc()
print(cal.add(20,50,60))
print(cal.add(20,50))
print(cal.add(20))
        