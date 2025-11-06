# shallow copy
import copy

# a = [1,2,3,[10,20]]
# b=copy.copy(a)

# print("before")
# print("a",a)
# print("b",b)

# b[0] = 100
# b[3][0] = 999
# print("after")
# print("a",a)
# print("b",b)



a = [1,2,3,[10,20]]
b=copy.deepcopy(a)

print("before")
print("a",a)
print("b",b)

b[0] = 100
b[3][0] = 999
print("after")
print("a",a)
print("b",b)