# Systax Error

# if True:
#     print("Hello")

# Tab error
if True:
    print("Hello")

# not defined
# print(a)
# 
# #unbound local error
# a=10
# def test():
#     print(a)
#     # a+=1
# test()


# typo error
# num = 5+"10"
# print(num)


# value error
# usrinput = int(input)

# # ZeroDivisionError
# print(5/0)

# index error
# list = [10,20]
# print(list[3])


try:
    num = int(input("Enter the number"))
    print(5/num)
except ZeroDivisionError:
    print("Don't use zero")
except ValueError:
    print("Please enter only number")