# def greet():
#     print("Welcome to Python")

# greet()

# def add(a,b):
#     print(a+b)

# add(50,66)
# add(50,80)

# # default
# def newadd(a=22,b=35):
#     print(a+b)

# newadd()
# newadd(50,66)

# keyword Arguments
# def user(name,age):
#     print(name,age)

# user(age=20,name="abc")

# def multiple(a,b):
#     return a*b

# print(multiple(2,3))

# # variable length arguments
# def show(*names): #names ["xyz","abc","def"]
#     for name in names: # 1:#name = xyz #2:name = abc 3.name = def
#         print(name)

# show("xyz","abc","def")
# show("hello","World","This","is","Python")

# ananoums function
# # lambda
# square = lambda x,y:x*y
# print(square(2,3))

# # local scope
# def newValue():
#     d=50
#     print(d)
# # print(d)
# newValue()
# global scope
# d=60
# def valueD(d):
#     print(d)

# valueD(int(input("Enter the number to print:")))


def greet():
    print("Welcome")
