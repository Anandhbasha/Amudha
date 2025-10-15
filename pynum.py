import numpy as np

# # 1D array

# arr1 = np.array([10,20,30,40])

# print(arr1)

# # 2d array

# arr2 = np.array([[20,50,60],[444,888,777]])

# print(arr2)

# # 3d array
# arr3 = np.array([[4,5,7],[5,8,9],[0,5,8]])
# print(arr3)

# zero
# z = np.zeros((3,4))
# print(z)

# o = np.ones((4,3))
# print(o)

# e = np.eye(3)
# print(e)

# range array
# rangelist = np.arange(0,10,2)
# print(rangelist)

# # equal interval
# linespace = np.linspace(0,1,5)
# print(linespace)


# rand array
# rands = np.random.rand(2,2) 
# print(rands)

# randsint = np.random.randint(1,10, size=(2,2))
# print(randsint)


arr3 = np.array([[4,5,7],[5,8,9],[0,5,8]])
# print(arr3[0])
# print(arr3[0:2])
arr3[1,2] = 60
# print(arr3)
# print(arr3[1,2])
# print(arr3[:,2])

# sub matrix
# print(arr3[0:2,1:3])


# filter
# print(arr3[arr3>20])

# list1 = np.array([20,41,52])
# list2 = np.array([22,88,99])
# print(list1+list2)
# print(list1*list2)
# print(list1**2)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
dots = np.dot(a,b)

# transpose
# print(dots.T)
# print(np.sum(a))
# mean
# print(np.mean(dots))
# print(np.average(dots))

print(np.max(dots))
print(np.min(dots))

# reshape
flat = np.arange(0,12)
reshapes = flat.reshape(3,4)
print(reshapes)

newflat = reshapes.flatten()
print(newflat)

