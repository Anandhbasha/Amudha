# def norfunction(n):
#     res = []
#     for i in range (1,n+1):
#         res.append(i)
#     return res
# print(norfunction(5))
# print(norfunction(8))

# def genFunction(n):
#     for i in range(1,n+1):
#         yield i

# for num in genFunction(5):
#     print(num)


# def greet(func):
#     def wrapper():
#         print("Hello World")
#         func()
#         print("Have a nice day")
#     return wrapper

# @greet
# def sayHi():
#     print("I am a developer")

# sayHi()





# deep copy


a = [1,2,3]
b=copy.deepcopy(a)

print("before")
print("a",a)
print("b",b)

b[0] = 999
print("after")
print("a",a)
print("b",b)