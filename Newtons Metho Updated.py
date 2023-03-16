import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
from math import log, exp, sin, cos, sqrt, tan
import math
from scipy.misc import derivative



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

def maxFunction(Table):
    
    max = Table[0,1]
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] >= max:
            max = Table[i,1]
    return(max)

#//////////////////////////////////////////////////////////////////////////////

def minFunction(Table):
    
    min = Table[0,1]
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] <= min:
            min = Table[i,1]
    return(min)

#//////////////////////////////////////////////////////////////////////////////

def fprime(f,x):
    # Takes in some function, f evaluatd at the point x
    Δx = 2**-32
    Δy = f(x+Δx) - f(x)
    return(Δy/Δx)
#//////////////////////////////////////////////////////////////////////////////

def NewtonsMethod(f, a, b, x, ε):
    
    if f(a)*f(b) < 0 and (b-a) > 0 and a < x and x < b and ε > 0:
        
        # Table of values for f(x) and f'(x)
        function, FirstDerivative, SecondDerivative = SecondDerivativePlot(f,a,b)
    
        minSlope = minFunction(abs(FirstDerivative))
        maxConcavity = maxFunction(abs(SecondDerivative))
        
        print(minSlope)
        print(maxConcavity)
        
        if 0 != minSlope and 0 != maxConcavity and 1 < (ε*maxConcavity)/(2*minSlope) and 1 < (b-a)*maxConcavity/(2*minSlope): #and 2 < (maxConcavity*ε)/minSlope :
        
            # n calculates the number of itterations needed to ensure an arrorr of ε on the interval [a,b]
            n = math.ceil(math.log( (math.log( (ε*maxConcavity)/(2*minSlope) ))/(math.log( (b-a)*maxConcavity/(2*minSlope) )) ,2 ) - 1)
            
            # This will create a sequence of itterations  
            values = []
           
            for i in range(1,n+1):
            
                x  = x - f(x)/fprime(f,x)
                values.append(x)
                
            Itterations = array(values,float)    
            print(n, "Itterations to get a value of",x)
            return Itterations
        
        else:
            
            print("something went wrong in second if")
            
    else:
        
        print("something went wrong in first if")
        
#//////////////////////////////////////////////////////////////////////////////

def f(x):
    return x**3+2*x-54
#//////////////////////////////////////////////////////////////////////////////
            
        

K = NewtonsMethod(f, 3, 4, 3.5, 10**-8) 
 


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
from math import log, exp, sin, cos, sqrt, tan
import math
from scipy.misc import derivative



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
        
        plt.plot(xCoordinate, yCoordinate, c = 'red', label = 'function')
        plt.plot(xCoordinate, slope1, c = 'blue', label = 'first derivative')
        plt.plot(xCoordinate, slope2, c = 'green', label = 'second derivative')
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.legend()
        plt.show()
        
        return transpose(function), transpose(FirstDerivative), transpose(SecondDerivative)
#//////////////////////////////////////////////////////////////////////////////

def maxFunction(Table):
    
    max = Table[0,1]
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] >= max:
            max = Table[i,1]
    return(max)

#//////////////////////////////////////////////////////////////////////////////

def minFunction(Table):
    
    min = Table[0,1]
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] <= min:
            min = Table[i,1]
    return(min)

#//////////////////////////////////////////////////////////////////////////////

def fprime(f,x):
    # Takes in some function, f evaluatd at the point x
    Δx = 2**-32
    Δy = f(x+Δx) - f(x)
    return(Δy/Δx)
#//////////////////////////////////////////////////////////////////////////////

def NewtonsMethod(f, a, b, ε):
    
    # Table of values for f(x) and f'(x)
    function, FirstDerivative, SecondDerivative = SecondDerivativePlot(f,a,b)
    x = (b+a)/2
    
    if f(a)*f(b) < 0 and (b-a) > 0 and ε > 0 and minFunction(abs(FirstDerivative)) != 0:
    
        supremum = maxFunction(abs(SecondDerivative)/abs(2*FirstDerivative))
        print(supremum)
    
        if (ε*supremum != 1 and x*supremum != 1):
            
            # n calculates the number of itterations needed to ensure an arrorr of ε on the interval [a,b]
            n = math.ceil(math.log((math.log(ε*supremum)/(math.log( ((b-a)/2)*supremum ))),2)-1)
            
            # This will create a sequence of itterations  
            values = [x]
            for i in range(1,n+1):
            
                x  = x - f(x)/fprime(f,x)
                values.append(x)
                
            Itterations = array(values,float)    
            print(n, "Itterations to get a value of",x)
            return Itterations
        
        else:
            
            print("Invalid Interval")
    else:
        
        print("Cannot calculate an appropriate number of itterations on this interval")
        
#//////////////////////////////////////////////////////////////////////////////

def f(x):
    return exp(x) + x - 7
#//////////////////////////////////////////////////////////////////////////////
            
        

K = NewtonsMethod(f, 0, 2, 10**-8) 

