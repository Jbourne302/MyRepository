import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros
from math import log, exp, sin, cos, sqrt, tan

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

# Function to demonstrate eulers method

# This is for a function of 2 variables. Modify it for multiple variables
# This function also does all of the RK methods at once
def RK_Methods(function,initialTime,finalTime):
    
    steps = int(input("Enter number of steps: "))
    initialValue = float(input("Enter the initial value: "))
    
    # Make sure the time is non-negative
    if finalTime > initialTime and steps > 0:
           
        Δt = (finalTime - initialTime)/steps
        
        # This is what you should modify for more/less variables
        tCoordinates = [initialTime]
        Euler_yCoordinates = [initialValue]
        RK2_yCoordinates = [initialValue]
        RK3_yCoordinates = [initialValue]
        RK4_yCoordinates = [initialValue]
        
        
        # Loop to get the (t,y(t)) coordinates on each step
        for i in range(1,steps+1):
        
            # Regular Euler method setup
            yPrime = function(tCoordinates[i-1], Euler_yCoordinates[i-1])
            Euler_Δy = Δt*yPrime
            
            # RK2 setup
            temporary_Δy = Δt*yPrime
            temporary_y = RK2_yCoordinates[i-1] + temporary_Δy
            temporary_yPrime = function(tCoordinates[i-1] + Δt, temporary_y)
            actual_yprime = (temporary_yPrime + yPrime)/2
            RK2_Δy = Δt*actual_yprime
            
            
            # RK3 setup
            RK3_k1 = function(tCoordinates[i-1], RK3_yCoordinates[i-1])
            RK3_k2 = function(tCoordinates[i-1] + (1/2)*Δt, RK3_yCoordinates[i-1] + (1/2)*RK3_k1*Δt )
            RK3_k3 = function(tCoordinates[i-1] + Δt, RK3_yCoordinates[i-1] - RK3_k1*Δt + 2*RK3_k2*Δt )
            RK3_y = RK3_yCoordinates[i-1] + (1/6)*(RK3_k1+4*RK3_k2+RK3_k3)*Δt
            
            # RK4 setup
            RK4_k1 = function(tCoordinates[i-1], RK4_yCoordinates[i-1])
            RK4_k2 = function(tCoordinates[i-1] + (1/2)*Δt, RK4_yCoordinates[i-1] + (1/2)*RK4_k1*Δt )
            RK4_k3 = function(tCoordinates[i-1] + (1/2)*Δt, RK4_yCoordinates[i-1] + (1/2)*RK4_k2*Δt )
            RK4_k4 = function(tCoordinates[i-1] + Δt, RK4_yCoordinates[i-1] + RK4_k3*Δt )
            RK4_y = RK4_yCoordinates[i-1] + (1/6)*(RK4_k1+2*(RK4_k2+RK4_k3)+RK4_k4)*Δt
            
            # Add the calculated y coordinates to our lists
            Euler_yCoordinates.append(Euler_yCoordinates[i-1] + Euler_Δy)
            RK2_yCoordinates.append(RK2_yCoordinates[i-1] + RK2_Δy)
            RK3_yCoordinates.append(RK3_y)
            RK4_yCoordinates.append(RK4_y)
            tCoordinates.append(tCoordinates[i-1] + Δt)
        
        # Plot everything after we finished geting the coordinates
        plt.plot(tCoordinates, Euler_yCoordinates, c = 'red', label='Euler')
        plt.plot(tCoordinates, RK2_yCoordinates, c = 'blue', label='RK2')
        plt.plot(tCoordinates, RK3_yCoordinates, c = 'green', label='RK3')
        plt.plot(tCoordinates, RK4_yCoordinates, c = 'black', label='RK4')
        plt.ylabel('y(t)')
        plt.xlabel('time')
        plt.legend()
        plt.show()
        
        # Table of completed values
        CoordinateTable = array([tCoordinates,Euler_yCoordinates,RK2_yCoordinates,
                                 RK3_yCoordinates,RK4_yCoordinates],float)
        
        return(transpose(CoordinateTable))
    
    else:
        print("Invalid input")
    
#//////////////////////////////////////////////////////////////////////////////

# Function to demonstrate eulers method

# This is for a function of 2 variables. Modify it for multiple variables

def Eulers_Method(function,initialTime,finalTime):
    
    steps = int(input("Enter number of steps: "))
    initialValue = float(input("Enter the initial value: "))
    
    # Make sure the time is non-negative
    if finalTime > initialTime and steps > 0:
           
        Δt = (finalTime - initialTime)/steps
        
        # This is what you should modify for more/less variables
        yCoordinates = [initialValue]
        tCoordinates = [initialTime]
        
        # Loop to get the (t,y(t)) coordinates on each step
        for i in range(1,steps+1):
        
            # y'(t,y) = f(t,y)
            # This is the part you should modify for more/less variables
            yPrime = function(tCoordinates[i-1], yCoordinates[i-1])
            Δy = Δt*yPrime
            
            yCoordinates.append(yCoordinates[i-1] + Δy)
            tCoordinates.append(tCoordinates[i-1] + Δt)
        
        # Plot everything after we finished geting the coordinates
        plt.plot(tCoordinates, yCoordinates, c = 'red')
        plt.ylabel('y(t)')
        plt.xlabel('time')
        plt.show()
        
        CoordinateTable = array([tCoordinates,yCoordinates],float)
        return(transpose(CoordinateTable))
    
    else:
        print("Invalid input")
    
#//////////////////////////////////////////////////////////////////////////////

# Function to demonstrate RK2 method

# This is for a function of 2 variables. Modify it for multiple variables

def RK2(function,initialTime,finalTime):
    
    steps = int(input("Enter number of steps: "))
    initialValue = float(input("Enter the initial value: "))
    
    # Make sure the time is non-negative
    if finalTime > initialTime and steps > 0:
           
        Δt = (finalTime - initialTime)/steps
        
        # This is what you should modify for more/less variables
        yCoordinates = [initialValue]
        tCoordinates = [initialTime]
        
        # Loop to get the (t,y(t)) coordinates on each step
        for i in range(1,steps+1):
        
            # y'(t,y) = f(t,y)
            # This is the part you should modify for more/less variables
            yPrime = function(tCoordinates[i-1], yCoordinates[i-1])
            
            #Temporary values that makes RK2 work
            temporary_Δy = Δt*yPrime
            temporary_y = yCoordinates[i-1] + temporary_Δy
            temporary_yPrime = function(tCoordinates[i-1] + Δt, temporary_y)
            actual_yprime = (temporary_yPrime + yPrime)/2
            
            Δy = Δt*actual_yprime
            
            yCoordinates.append(yCoordinates[i-1] + Δy)
            tCoordinates.append(tCoordinates[i-1] + Δt)
        
        # Plot everything after we finished geting the coordinates
        plt.plot(tCoordinates, yCoordinates, c = 'green')
        plt.ylabel('y(t)')
        plt.xlabel('time')
        plt.show()
        
        CoordinateTable = array([tCoordinates,yCoordinates],float)
        return(transpose(CoordinateTable))
    
#//////////////////////////////////////////////////////////////////////////////

# Function to demonstrate RK3 method

# This is for a function of 2 variables. Modify it for multiple variables

def RK3(function,initialTime,finalTime):
    
    steps = int(input("Enter number of steps: "))
    initialValue = float(input("Enter the initial value: "))
    
    # Make sure the time is non-negative
    if finalTime > initialTime and steps > 0:
           
        Δt = (finalTime - initialTime)/steps
        
        # This is what you should modify for more/less variables
        yCoordinates = [initialValue]
        tCoordinates = [initialTime]
        
        # Loop to get the (t,y(t)) coordinates on each step
        for i in range(1,steps+1):
        
            # y'(t,y) = f(t,y)
            # This is the part you should modify for more/less variables
            
            k1 = function(tCoordinates[i-1], yCoordinates[i-1])
            k2 = function(tCoordinates[i-1] + (1/2)*Δt, yCoordinates[i-1] + (1/2)*k1*Δt )
            k3 = function(tCoordinates[i-1] + Δt, yCoordinates[i-1] - k1*Δt + 2*k2*Δt )
            y = yCoordinates[i-1] + (1/6)*(k1+4*k2+k3)*Δt
            
            yCoordinates.append(y)
            tCoordinates.append(tCoordinates[i-1] + Δt)
        
        # Plot everything after we finished geting the coordinates
        plt.plot(tCoordinates, yCoordinates, c = 'blue')
        plt.ylabel('y(t)')
        plt.xlabel('time')
        plt.show()
        
        CoordinateTable = array([tCoordinates,yCoordinates],float)
        return(transpose(CoordinateTable))
    
#//////////////////////////////////////////////////////////////////////////////

# Function to demonstrate RK4 method

# This is for a function of 2 variables. Modify it for multiple variables

def RK4(function,initialTime,finalTime):
    
    steps = int(input("Enter number of steps: "))
    initialValue = float(input("Enter the initial value: "))
    
    # Make sure the time is non-negative
    if finalTime > initialTime and steps > 0:
           
        Δt = (finalTime - initialTime)/steps
        
        # This is what you should modify for more/less variables
        yCoordinates = [initialValue]
        tCoordinates = [initialTime]
        
        # Loop to get the (t,y(t)) coordinates on each step
        for i in range(1,steps+1):
        
            # y'(t,y) = f(t,y)
            # This is the part you should modify for more/less variables
            
            k1 = function(tCoordinates[i-1], yCoordinates[i-1])
            k2 = function(tCoordinates[i-1] + (1/2)*Δt, yCoordinates[i-1] + (1/2)*k1*Δt )
            k3 = function(tCoordinates[i-1] + (1/2)*Δt, yCoordinates[i-1] + (1/2)*k2*Δt )
            k4 = function(tCoordinates[i-1] + Δt, yCoordinates[i-1] + k3*Δt )
            y = yCoordinates[i-1] + (1/6)*(k1+2*(k2+k3)+k4)*Δt
            
            yCoordinates.append(y)
            tCoordinates.append(tCoordinates[i-1] + Δt)
        
        # Plot everything after we finished geting the coordinates
        plt.plot(tCoordinates, yCoordinates, c = 'yellow')
        plt.ylabel('y(t)')
        plt.xlabel('time')
        plt.show()
        
        CoordinateTable = array([tCoordinates,yCoordinates],float)
        return(transpose(CoordinateTable))
    
#//////////////////////////////////////////////////////////////////////////////

def f(x,y):
    return y-x**2+1
#//////////////////////////////////////////////////////////////////////////////

def g(x,y):
    return (2*y + 0*x)
#//////////////////////////////////////////////////////////////////////////////


RK_Table = RK_Methods(g,0,2)
#Euler_Table = Eulers_Method(g,0,2)
#RK2_Table = RK2(g,0,2)
#RK3_Table = RK3(g,0,2)
#RK4_Table = RK4(g,0,2)
