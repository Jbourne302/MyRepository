from numpy import loadtxt
from math import exp,sin,cos,sqrt
import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
import numpy as np

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

def Trapizoid_Approximation(function,a,b,n):
    
    
    # This function gives the approximation of the inegral using the trapizoid rule
    def Trapezoid_Rule(function,a,b,n):
        
        # N is the number of trapezoids
        Δx = (b-a)/n
        Area = 0  
        
        for i in range(1,n+1):
        
            Area += (1/2)*Δx*( function( a+(i-1)*Δx ) + function( a+i*Δx ) )

        return(Area)
    

    # List of values to plot the function and its integral on the same axis
    Integral_xCoordinates = [a]
    Integral_yCoordinates = [Trapezoid_Rule(function,a,a,n)]
    function_xCoordinates = [a]
    function_yCoordinates = [function(a)]
    
    Δx = (b-a)/n
    
    for i in range(1,n+1):
        
        # Append the updated coordinates to each respective list
        Integral_xCoordinates.append(Integral_xCoordinates[i-1] + Δx)
        Integral_yCoordinates.append(Trapezoid_Rule(function,a,a+i*Δx,n))
        function_xCoordinates.append(function_xCoordinates[i-1] + Δx)
        function_yCoordinates.append(function(function_xCoordinates[i]))
        
    # Plot f(x) and F(x)
    plt.plot(Integral_xCoordinates, Integral_yCoordinates, c = 'red', label ='F(x)')
    plt.plot(function_xCoordinates, function_yCoordinates, c = 'blue', label ='f(x)')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    
    # Return the cummulative areas 
    CoordinateTable = array([Integral_xCoordinates,Integral_yCoordinates],float)
    return(transpose(CoordinateTable))
    
#//////////////////////////////////////////////////////////////////////////////

def Simpsons_Approximation(function,a,b,n):
    
    # This function gives the approximation of the inegral using the Simpson rule
    def Simpsons_Rule(function,a,b,n):
        
        if n%2 == 0:
            
            Δx = (b-a)/n
            Area = 0
        
            for i in range(1,int((n/2)+1)): 
                
                # Simpsons formula
                Area += (1/3)*Δx*( function( a+2*(i-1)*Δx ) + 4*function( a+(2*i-1)*Δx ) + function( a+2*i*Δx ) )
                       
            return(Area)
    

    # List of values to plot the function and its integral on the same axis
    Integral_xCoordinates = [a]
    Integral_yCoordinates = [Simpsons_Rule(function,a,a,n)]
    function_xCoordinates = [a]
    function_yCoordinates = [function(a)]
    
    Δx = (b-a)/n
    
    for i in range(1,n+1):
        
        # Append the updated coordinates to each respective list
        Integral_xCoordinates.append(Integral_xCoordinates[i-1] + Δx)
        Integral_yCoordinates.append(Simpsons_Rule(function,a,a+i*Δx,n))
        function_xCoordinates.append(function_xCoordinates[i-1] + Δx)
        function_yCoordinates.append(function(function_xCoordinates[i]))
        
    # Plot f(x) and F(x)
    plt.plot(Integral_xCoordinates, Integral_yCoordinates, c = 'red', label ='F(x)')
    plt.plot(function_xCoordinates, function_yCoordinates, c = 'blue', label ='f(x)')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    
    # Return the cummulative areas 
    CoordinateTable = array([Integral_xCoordinates,Integral_yCoordinates],float)
    return(transpose(CoordinateTable))
    
#//////////////////////////////////////////////////////////////////////////////

def Riemann_Approximation(function,a,b,n,user_input):
    
    # This function gives the approximation of the inegral using the Riemann rule
    def Riemann_Rule(f,a,b,n):
        
        if n%1 == 0 and a <= b:
        
            Δx = (b-a)/n
            Area = 0   
            sum_type = user_input.capitalize()
            
            if sum_type == 'Left':
                
                for i in range(1,n+1):
                    Area += f(a + Δx*(i-1))*Δx
            
            elif sum_type == 'Right':
                
                for i in range(1,n+1):
                    Area += f(a + Δx*i)*Δx
            
            elif sum_type == 'Midpoint':
                
                for i in range(1,n+1):
                    Area += f(a + (Δx/2)*(2*i-1))*Δx
            else:
                print("Could not understand input.")
                    
            return(Area)
            
        else:
            print("Invalid input")
    

    # List of values to plot the function and its integral on the same axis
    Integral_xCoordinates = [a]
    Integral_yCoordinates = [Riemann_Rule(function,a,a,n)]
    function_xCoordinates = [a]
    function_yCoordinates = [function(a)]
    
    Δx = (b-a)/n
    
    for i in range(1,n+1):
        
        # Append the updated coordinates to each respective list
        Integral_xCoordinates.append(Integral_xCoordinates[i-1] + Δx)
        Integral_yCoordinates.append(Riemann_Rule(function,a,a+i*Δx,n))
        function_xCoordinates.append(function_xCoordinates[i-1] + Δx)
        function_yCoordinates.append(function(function_xCoordinates[i]))
        
    # Plot f(x) and F(x)
    plt.plot(Integral_xCoordinates, Integral_yCoordinates, c = 'red', label ='F(x)')
    plt.plot(function_xCoordinates, function_yCoordinates, c = 'blue', label ='f(x)')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    
    # Return the cummulative areas 
    CoordinateTable = array([Integral_xCoordinates,Integral_yCoordinates],float)
    return(transpose(CoordinateTable))

#//////////////////////////////////////////////////////////////////////////////

def relativeError(absolute,exact):
    
    if exact != 0:
        return(absolute/exact)
    
def absoluteError(measured,exact):
    
        return(abs(measured-exact))
    
#//////////////////////////////////////////////////////////////////////////////
    
def f(x):
    return exp(x**2)
#//////////////////////////////////////////////////////////////////////////////
def h(x):
    return(3*x**2)
#//////////////////////////////////////////////////////////////////////////////
def E(x):
    
    def g(x):
        return(exp(-x**2))
    
    n = int(input("Enter number of steps: "))
    
    if n > 0:
        return(Simpsons_Approximation(g,0,x,n))

#//////////////////////////////////////////////////////////////////////////////

def combine_Arrays(a,b,c):
    
    # Concatenate the arrays
    combined_array = np.concatenate((a, b[:, 1:],c[:, 1:]), axis=1)
    
    # Remove any duplicate columns
    unique_array = np.unique(combined_array, axis=1)
    
    # Print the final array
    return(unique_array)

#//////////////////////////////////////////////////////////////////////////////


Trapizoid_Table = Trapizoid_Approximation(f,0,2,128)
Simpsons_Table = Simpsons_Approximation(f,0,2,128)
Riemann_Table = Riemann_Approximation(f,0,2,128,'midpoint')

#Table = combine_Arrays(Riemann_Table,Trapizoid_Table,Simpsons_Table)
 
    




