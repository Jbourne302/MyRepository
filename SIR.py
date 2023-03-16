import matplotlib.pyplot as plt
from numpy import array
from numpy import zeros

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

# returns the values of S,I, and R, t units after the initial
def daysAfterS(t,Table):
    return(Table[t,1])

def daysAfterI(t,Table):
    return(Table[t,2])

def daysAfterR(t,Table):
    return(Table[t,3])

#//////////////////////////////////////////////////////////////////////////////

# creates a peicewise function that returns the values for S after after n steps 
def piecewiseLinearS(x,Table):
    
    values = []
    
    # Make sure x is in the domain
    if Table[0,0] <= x and x <= Table[Table.shape[0]-1,0]:
    
        for i in range(1,Table.shape[0]):
            
            # Compute the changes in x and y for calculating slope
            Δx = Table[i,0] - Table[i-1,0] 
            Δy = Table[i,1] - Table[i-1,1]
            
            values.append( (Δy/Δx)*( x - Table[i-1,0] ) + Table[i-1,1] )  
            
            if Table[i-1,0] <= x and x <= Table[i,0]:
                return(values[i-1])
            
#//////////////////////////////////////////////////////////////////////////////
            
# creates a peicewise function that returns the values for I after n steps            
def piecewiseLinearI(x,Table):
    
    values = []
    
    # Make sure x is in the domain
    if Table[0,0] <= x and x <= Table[Table.shape[0]-1,0]:
    
        for i in range(1,Table.shape[0]):
            
            # Compute the changes  in x and y for calculating slope
            Δx = Table[i,0] - Table[i-1,0] 
            Δy = Table[i,2] - Table[i-1,2]
            
            values.append( (Δy/Δx)*( x - Table[i-1,0] ) + Table[i-1,2] )  
            
            if Table[i-1,0] <= x and x <= Table[i,0]:
                return(values[i-1])
            
#//////////////////////////////////////////////////////////////////////////////

# creates a peicewise function that returns the values for R after n steps            
def piecewiseLinearR(x,Table):
    
    values = []
    
    # Make sure x is in the domain
    if Table[0,0] <= x and x <= Table[Table.shape[0]-1,0]:
    
        for i in range(1,Table.shape[0]):
            
            # Compute the changes in x and y for calculating slope
            Δx = Table[i,0] - Table[i-1,0] 
            Δy = Table[i,3] - Table[i-1,3]
            
            values.append( (Δy/Δx)*( x - Table[i-1,0] ) + Table[i-1,3] )  
            
            if Table[i-1,0] <= x and x <= Table[i,0]:
                return(values[i-1])            

#//////////////////////////////////////////////////////////////////////////////

# Returns the max of S
def maxS(Table):
    
    max = Table[0,1]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] >= max:
            max = Table[i,1]
            t = i
    return(Table[t,0],max)

#//////////////////////////////////////////////////////////////////////////////

# Returns the max of I
def maxI(Table):
    
    max = Table[0,2]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,2] >= max:
            max = Table[i,2]
            t = i
    return(Table[t,0],max)

#//////////////////////////////////////////////////////////////////////////////

# Returns the max of R
def maxR(Table):
    
    max = Table[0,3]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,3] >= max:
            max = Table[i,3]
            t = i
    return(Table[t,0],max)

#//////////////////////////////////////////////////////////////////////////////

# Returns the min of S
def minS(Table):
    
    min = Table[0,1]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,1] <= min:
            min = Table[i,1]
            t = i
    return(Table[t,0],min)

#//////////////////////////////////////////////////////////////////////////////

# Returns the min of I
def minI(Table):
    
    min = Table[0,2]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,2] <= min:
            min = Table[i,2]
            t = i
    return(Table[t,0],min)

#//////////////////////////////////////////////////////////////////////////////

# Returns the min of R
def minR(Table):
    
    min = Table[0,3]
    t = 0
    
    for i in range(1,Table.shape[0]):
        if Table[i,3] <= min:
            min = Table[i,3]
            t = i
    return(Table[t,0],min)

#//////////////////////////////////////////////////////////////////////////////

# SIR generator (suceptible, infected, recovered)
def SIR(initialTime,finalTime,S,I,R):
    
    steps = int(input("Enter number of steps: "))
    
    if initialTime >= 0 and finalTime >= 0 and finalTime > initialTime and steps > 0:
    
        Δt = (finalTime - initialTime)/steps
        
        # Edit this for different functions
        initialSprime = -.00001*S*I
        initialIprime = .00001*S*I - I*0.08
        initialRprime = I*0.08
        
        # initial Derivatives
        SprimeCoordinates = [initialSprime]
        IprimeCoordinates = [initialIprime]
        RprimeCoordinates = [initialRprime]
        
        # initial coordinates
        discrepancy = [0]
        tCoordinates = [initialTime]
        SCoordinates = [S]
        ICoordinates = [I]
        RCoordinates = [R]
        
        for i in range(1,steps+1):
             
            # Rates
            # Edit this for different functions
            Sprime = -.00001*SCoordinates[i-1]*ICoordinates[i-1]
            Iprime = .00001*SCoordinates[i-1]*ICoordinates[i-1] - ICoordinates[i-1]*(0.08)
            Rprime = ICoordinates[i-1]*(0.08)
            
            # Changes
            ΔS = Δt*Sprime
            ΔI = Δt*Iprime
            ΔR = Δt*Rprime
            
            # Derivatives
            SprimeCoordinates.insert(i, Sprime)
            IprimeCoordinates.insert(i, Iprime)
            RprimeCoordinates.insert(i, Rprime)
            
            # Coordinates
            SCoordinates.append(SCoordinates[i-1] + ΔS)
            ICoordinates.append(ICoordinates[i-1] + ΔI)
            RCoordinates.append(RCoordinates[i-1] + ΔR)
            tCoordinates.append(tCoordinates[i-1] + Δt)
            discrepancy.append(SCoordinates[i] - SCoordinates[i-1])
        
    # Plot each graph as a function of t
    plt.plot(tCoordinates, SCoordinates, c = 'red', label='Suceptible')
    plt.plot(tCoordinates, ICoordinates, c = 'blue', label='Infected')
    plt.plot(tCoordinates, RCoordinates, c = 'green', label='Recovered')
    plt.ylabel('Values')
    plt.xlabel('time')
    plt.legend()
    plt.show()
    
    # |Time|Susceptible|Infected|Recovered|S'|I'|R'|Discrepancy|
    CoordinateTable = array([tCoordinates,SCoordinates,ICoordinates,
                             RCoordinates,SprimeCoordinates,IprimeCoordinates,
                             RprimeCoordinates,discrepancy],float)
    
    return(transpose(CoordinateTable))

#//////////////////////////////////////////////////////////////////////////////

Table = SIR(0,20,45000,2100,500)

print(maxI(Table))



