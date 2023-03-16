# Useful imports
import numpy as np
import matplotlib.pyplot as plt
from math import log, exp, sin, cos, sqrt, pi, e


#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

# Creating arrays
numberOfElements = int(input("Enter the length of the list: "))
a = np.zeros(numberOfElements, float)
print(a)

t = np.empty(4, float)
print(t)

r = [1.0, 1.5, -2.2]
a = np.array(r, float)

a = np.array([[1, 2, 3], [4, 5, 6]], int)
print(a)

a = np.zeros([2, 2], int)
a[0, 1] = 1
a[1, 0] = -1
print(a)

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

# Useful arithmetic

# x = float(input("Enter the value of x: "))
# Exponents: x**y           [===>]  x^y
# Integer part of x/y       [===>]  x//y = floor(x/y)
# Remainder of x/y          [===>]  x%y
# x/y = x//y + (x%y)/y
# math.log(argument,base)   [===>]  math.log(y,x)


#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

# If statements

x = int(input("Enter a whole number no greater than ten: "))

if x > 10:
    print("You entered a number greater than ten.")
    print("Let me fix that for you.")
    x = 10
print("Your number is", x)


#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////


# Arrays vs Lists

# a.size returns the product of the dimensions of an array, a
# a.shape returns the dimensions of an array, a in the form (row, col)
# Arrays start counting at 0. so, a[n] returns the (n+1)th element of a
# the map(x,y) takes a function x, and applies it to every element in a

# Pro list
# 1) The number of elements in an array is fixed. You cannot add elements to an array once it is created, or remove them
# 2) The elements of an array must all be of the same type, such as all floats or all integers. You cannot mix elements of different types in the same array and you cannot change the type of the elements once an array is created

# Pro array
# 1) Arrays can be two-dimensional, like matrices in algebra
# 2) Arrays behave roughly like vectors or matrices


#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

# Plotting

# plt.plot([List of values], c = [color], label = [Title])
# plt.ylabel([y axis title])
# plt.xlabel([x axis title])
# plt.legend()
# plt.show()

#//////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////

# Derivatives of functions

#from scipy.misc import derivative

#df_dx = derivative(f, x0=1.0, dx=1e-8, n=1)


