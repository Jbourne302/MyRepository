from math import log,exp,sin,cos,sqrt

#//////////////////////////////////////////////////////////////////////////////

def NewtonsMethod(function,initial):
    
    def fprime(f,x):
        # Takes in some function, f evaluatd at the point x
        Δx = 2**-32
        Δy = f(x+Δx) - f(x)
        return(Δy/Δx)   
    
    values = [initial]
    
    for i in range(1,8):
        values.append( values[i-1] -  function(values[i-1]) / fprime(function,values[i-1]) )
        
    return(values)

#//////////////////////////////////////////////////////////////////////////////

def f(x):
    return(x**2-2)

def g(x):
    return(log(x)-1)

#//////////////////////////////////////////////////////////////////////////////

d = NewtonsMethod(f,1)
o = NewtonsMethod(g,0.5)
