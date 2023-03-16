from math import log,exp,sin,cos,sqrt
import matplotlib.pyplot as plt

#//////////////////////////////////////////////////////////////////////////////

def ArcLength(function,xInitial,xFinal):

    steps = int(input("Enter number of steps: "))
    
    if xFinal > xInitial and steps > 0 and steps%1 == 0:
        
        Δx = (xFinal - xInitial)/steps
        distance = 0
            
        x1 = xInitial
        y1 = function(x1)
        x2 = x1 + Δx
        y2 = function(x2)
            
        xCoordinate = [x1]
        yCoordinate = [y1]
            
        while x2 <= xFinal:
                
            distance += sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
                
            x1 = x2
            y1 = function(x1)
            x2 += Δx
            y2 = function(x2)
                
            xCoordinate.append(x1)
            yCoordinate.append(y1)
                
        plt.plot(xCoordinate, yCoordinate, c = 'red')
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.show()
        return(distance)
    
#//////////////////////////////////////////////////////////////////////////////
        
def f(x):
    return(((2/3)*(x-1)**(3/2)))

#//////////////////////////////////////////////////////////////////////////////
 
A = ArcLength(f,1,7)

