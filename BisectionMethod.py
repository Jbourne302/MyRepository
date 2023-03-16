import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
from math import log,exp,sin,cos,sqrt,tan
import math

#//////////////////////////////////////////////////////////////////////////////
# TRANSPOSE FUNCTION

def transpose(x):
   
    # Row vectors have no value for its column length, so the length of its size is treated as 1
    if len(x.shape) == 2:
        
        # If we have a column, or regular matrix, transpose normally.
        if x.shape[0] >= 1 and x.shape[1] >= 1:
            # Get the dimension of the matrix
            numRow = x.shape[0]
            numCol = x.shape[1]
            # Create a matrix of zeros with swapped dimensions of x
            transposedMatrix = zeros([numCol,numRow],float)
            
            # Loop through each column at a time
            for n in range(0,numCol):
                for m in range(0,numRow):
                    # Swap the rows and columns
                    transposedMatrix[n,m] = x[m,n]         
                    
            return transposedMatrix
    else:
        transposedMatrix = zeros([x.shape[0],1],float)
        for n in range(0,x.shape[0]):
            transposedMatrix[n,0] = x[n]
        
        return transposedMatrix  
    
#//////////////////////////////////////////////////////////////////////////////

# Based on a given number of itterations, n
def Bisect1(f,a,b,n):
        
    if f(a)*f(b) < 0 and (b-a) > 0:
        
        # List to hold the values at each iteration
        values = []

        for i in range(1,n+1):
            
            x = (a+b)/2
            values.append(x)
            
            # Shorten the interval if f(x) has a different sign than f(a)/f(b)
            if f(a)*f(x) < 0:
                b = x
                
            elif f(x)*f(b) < 0:
                a = x
            # Found an exact value 
            else:
                break
                
        # Matrix that holds all of the itterations
        Itterations = array(values,float)
        
        print(n, "Itterations to get a value of",Itterations[Itterations.size-1])
        return Itterations
   
    else:
        print("Invalid interval entered")

#//////////////////////////////////////////////////////////////////////////////

# Based on a given tolorence, ε
def Bisect(f,a,b,ε):
        
    if f(a)*f(b) < 0 and (b-a) > 0:
        
        # List to hold the values at each iteration
        values = []
        
        # This is the number of steps to get an error within ε of the true value
        # Error is given by (b-a)/2^(n+1) < ε
        n = math.ceil(math.log((b-a)/(2*ε),2))

        for i in range(1,n+1):
            
            x = (a+b)/2
            values.append(x)
            
            # Shorten the interval if f(x) has a different sign than f(a)/f(b)
            if f(a)*f(x) < 0:
                b = x
                
            elif f(x)*f(b) < 0:
                a = x
            # Found an exact value 
            else:
                break
                
        # Matrix that holds all of the itterations
        Itterations = array(values,float)
        
        print(n, "Itterations to get a value of",Itterations[Itterations.size-1])
        return Itterations
   
    else:
        print("Invalid interval entered")

#//////////////////////////////////////////////////////////////////////////////

def f(x):
    return x**3-30*x**2+255

def g(x):
    return x**(1/2)-1.1
#//////////////////////////////////////////////////////////////////////////////
    
A = Bisect(g,0,2,10**-8)
