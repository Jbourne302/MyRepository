import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
from math import log, exp, sin, cos, sqrt, tan
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

def derivativePlot(function,xInitial,xFinal):

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
        slopes = [m]
            
        while x2 <= xFinal:
                
            x1 = x2
            y1 = function(x1)
            x2 += Δx
            y2 = function(x2)
            m = (y2-y1)/(x2-x1)
                
            xCoordinate.append(x1)
            yCoordinate.append(y1)
            slopes.append(m)
                
        function = array([xCoordinate,yCoordinate],float)
        FirstDerivative = array([xCoordinate,slopes],float)
        
        #plt.plot(xCoordinate, yCoordinate, c = 'red')
        #plt.plot(xCoordinate, slopes, c = 'blue')
        #plt.ylabel('f(x)')
        #plt.xlabel('x')
        #plt.show()
        return transpose(function), transpose(FirstDerivative)
#//////////////////////////////////////////////////////////////////////////////

def maxFunction(Table):
    
    max = Table[0,1]
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] >= max:
            max = Table[i,1]
    return(max)

#//////////////////////////////////////////////////////////////////////////////

# Given a function, f, on an interval [a,b] with tolerence less than ε and initial guess of x
def fixedPoint(f, a, b, x, ε):

    # Make sure that the function, f, satisfies a <= f(a) and f(b) <= b 
    if a <= f(a) and f(b) <= b and a <= x and x <= b and b-a > 0:
        
        # Table of values for f(x) and f'(x)
        function, derivative = derivativePlot(f,a,b)
        maxSlope = maxFunction(abs(derivative))
        
        # This is just to plot our functions
        plt.plot(transpose(function)[0,], transpose(function)[1,], c = 'red', label='Fucntion')
        plt.plot(transpose(derivative)[0,], transpose(abs(derivative))[1,], c = 'blue', label='Derivative')
        plt.plot(transpose(function)[0,], transpose(function)[0,], c = 'green', label='y=x')
        plt.xlabel('x')
        plt.legend()
        plt.show()
        
        # Make sure that |f'(x)| < 1
        if 0 < maxSlope and maxSlope < 1:
            
            # Calculate x1 with an initial guess of x
            x1 = f(x)
            Δx = abs(x-x1)
            
            # Use the error bound to calculate the max number of itterations 
            n = math.ceil(math.log(ε*(1-maxSlope)/Δx, maxSlope))
        
            # This will create a sequence of itterations 
            values = [] 
            
            for i in range(1,n+1):
                
                x = f(x)
                values.append(x)
                
            Itterations = array(values,float)
            print(n, "Itterations to get a value of",x)
            
            return Itterations
        
        else:
            print("|f'(x)| is not bounded by",maxSlope )
    
    else:
        print("Invalid interval and/or f(x) does not satisfy a <= f(a) and f(b) <= b")

#//////////////////////////////////////////////////////////////////////////////
def f(x):
    return math.log(7-x)
#//////////////////////////////////////////////////////////////////////////////

A = fixedPoint(f, 0, 2, 1.1, 10**-8)