#//////////////////////////////////////////////////////////////////////////////
# FACTORIAL FUNCTION
def factorial(n):
    
    x = 1
    
    if n >= 1: 
        if n%1 == 0:
            for y in range(1, n+1):
                x *= y     
        return x
    
    if n == 0:
        return 1
        

# Ask the user for input 
x = int(input("What do you want to find the factorial of? "))

# Make sure the user enter a non-positive integer
while x < 0 or x%1 != 0:
    x = int(input("Please enter a non-negative integer "))

print(x, "factorial is", factorial(x))


#//////////////////////////////////////////////////////////////////////////////
# TRANSPOSE FUNCTION

from numpy import array
from numpy import zeros

a = array([[1,2,34,4],[4,5,4,6],[7,4,8,9]], int)
b = array([1,2,34,4], int)
c = array([[1],[2],[34],[4]], int)
           
def transpose(x):
   
    # Row vectors have no value for its column length, so the length of its size is treated as 1
    if len(x.shape) == 2:
        
        # If we have a column, or regular matrix, transpose normally.
        if x.shape[0] >= 1 and x.shape[1] >= 1:
            # Get the dimension of the matrix
            numRow = x.shape[0]
            numCol = x.shape[1]
            # Create a matrix of zeros with swapped dimensions of x
            transposedMatrix = zeros([numCol,numRow],int)
            
            # Loop through each column at a time
            for n in range(0,numCol):
                for m in range(0,numRow):
                    # Swap the rows and columns
                    transposedMatrix[n,m] = x[m,n]         
                    
            return transposedMatrix
    else:
        transposedMatrix = zeros([x.shape[0],1],int)
        for n in range(0,x.shape[0]):
            transposedMatrix[n,0] = x[n]
        
        return transposedMatrix    
# End of transpose(x)
#//////////////////////////////////////////////////////////////////////////////

# Derivative

def fprime(x,f):
    # Takes in some function, f evaluatd at the point x
    Δx = 2**-32
    Δy = f(x+Δx) - f(x)
    return(Δy/Δx)   

#//////////////////////////////////////////////////////////////////////////////

def relativeError(absolute,exact):
    
    if exact != 0:
        return(abs(absolute/exact))
    
def absoluteError(measured,exact):
    
        return(abs(measured-exact))
    
#//////////////////////////////////////////////////////////////////////////////

import numpy as np

def combine_Arrays(a,b,c):
    
    # Concatenate the arrays
    combined_array = np.concatenate((a, b[:, 1:],c[:, 1:]), axis=1)
    
    # Remove any duplicate columns
    unique_array = np.unique(combined_array, axis=1)
    
    # Print the final array
    return(unique_array)

#//////////////////////////////////////////////////////////////////////////////

#//////////////////////////////////////////////////////////////////////////////

def SecondDerivativePlot(function,xInitial,xFinal):

    steps = 999999
    
    if xFinal > xInitial and steps > 0 and steps%1 == 0:
        
        Δx = (xFinal - xInitial)/steps        
        x1 = xInitial
        y1 = function(x1)
        x2 = x1 + Δx
        y2 = function(x2)
        m1 = (y2-y1)/(x2-x1)
        m2 = (y2-2*y1+function(x1-Δx))/(x2-x1)**2
        
        xCoordinate = [x1]
        yCoordinate = [y1]
        slope1 = [m1]
        slope2 = [m2]
        
        while x2 <= xFinal:
             
            x1 = x2
            x2 += Δx
            y3 = y1
            y2 = function(x2)
            y1 = function(x1)
            m1 = (y2-y1)/(x2-x1)
            m2 = (y2-2*y1+y3)/(x2-x1)**2
                
            xCoordinate.append(x1)
            yCoordinate.append(y1)
            slope1.append(m1)
            slope2.append(m2)
                
        function = array([xCoordinate,yCoordinate],float)
        FirstDerivative = array([xCoordinate,slope1],float)
        SecondDerivative = array([xCoordinate,slope2],float)
        
        plt.plot(xCoordinate, yCoordinate, c = 'red')
        plt.plot(xCoordinate, slope1, c = 'blue')
        plt.plot(xCoordinate, slope2, c = 'green')
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.show()
        
        return transpose(function), transpose(FirstDerivative), transpose(SecondDerivative)
#//////////////////////////////////////////////////////////////////////////////




#//////////////////////////////////////////////////////////////////////////////
import matplotlib.pyplot as plt

def FirstDerivativePlot(function,xInitial,xFinal):

    steps = 999999
    
    if xFinal > xInitial and steps > 0 and steps%1 == 0:
        
        Δx = (xFinal - xInitial)/steps        
        x1 = xInitial
        y1 = function(x1)
        x2 = x1 + Δx
        y2 = function(x2)
        m = (y2-y1)/(x2-x1)
        
        xCoordinate = [x1]
        yCoordinate = [y1]
        slope = [m]
        
        while x2 <= xFinal:
             
            x1 = x2
            x2 += Δx
            y2 = function(x2)
            y1 = function(x1)
            m = (y2-y1)/(x2-x1)
                
            xCoordinate.append(x1)
            yCoordinate.append(y1)
            slope.append(m)
                
        function = array([xCoordinate,yCoordinate],float)
        FirstDerivative = array([xCoordinate,slope],float)
        
        plt.plot(xCoordinate, yCoordinate, c = 'red', label='Function')
        plt.plot(xCoordinate, slope, c = 'blue', label='Derivative')
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.legend()
        plt.show()
        
        return transpose(function), transpose(FirstDerivative)
#//////////////////////////////////////////////////////////////////////////////