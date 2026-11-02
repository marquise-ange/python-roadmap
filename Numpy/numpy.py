#numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
#we do not need to install numpy as it is already installed in the colab environment
#we do import numpy as np to use the functions of numpy library

import numpy as np
my_list = [1,2,3,4]
my_array = np.array(my_list, dtype=np.float32)
print(my_list)
print(my_array)


#property size -> returns the total number of elements in the array
print("Size:", my_array.size) #output: 4

#property shape -> is a tuple of integers indicating the size of the array in each dimension
print("Shape:", my_array.shape) #output: (4,)

#property dtype -> returns the data type of the array
print("Dtype:", my_array.dtype) #output: float32

#property ndim(number of dimensions)
print("Number of dimensions:", my_array.ndim) #output: 1

#property itemsize -> returns the size (in bytes) of each element in the array
print("Item size:", my_array.itemsize) #output: 4

#astype -> is used to convert the data type of the array
my_array_int = my_array.astype(np.int32)
print("Converted array:", my_array_int) #output: [1 2 3 4]

#linespace -> returns evenly spaced numbers over a specified interval
linspace_array = np.linspace(0, 10, num=5)
print("Linspace array:", linspace_array) #output: [ 0.   2.5  5.   7.5 10. ]

 #arange -> returns evenly spaced values within a given interval(step not mentioned that is equal to 1)
arange_array = np.arange(0, 10, step=2)
print("Arange array:", arange_array) #output: [0 2 4 6 8]

#random-> is a module but have many  functions
#random.rand -> returns an array of given shape and fills it with random values between 0 and 1
random_array = np.random.rand(2, 3)
print("Random array:", random_array) #output: [[0.5488135  0.71518937 0.60276338] [0.02010739 0.96990985 0.83244264]]

#random.randint -> returns an array of given shape and fills it with random integers between low (inclusive) and high (exclusive)
random_int_array = np.random.randint(0, 10, size=(2, 3))
print("Random integer array:", random_int_array) #output: [[3 7 2] [5 1 9]]

#random.randn -> returns an array of given shape and fills it with random values from a standard normal distribution (mean=0, std=1)
random_normal_array = np.random.randn(2, 3)
print("Random normal array:", random_normal_array) #output: [[-0.41675785  1.38267189  0.63992102] [ 0.73246855 -0.24643149  0.0592874 ]]

#random.ranf -> returns an array of given shape and fills it with random values between 0 and 1
random_ranf_array = np.random.ranf((2, 3))
print("Random ranf array:", random_ranf_array) #output: [[0.39804426 0.73799541 0.18249173] [0.17545176 0.53155137 0.53182759]]

