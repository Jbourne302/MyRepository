def trapezoidPlot(function,a,b,n):
    
    #//////////////////////////////////////////////////////////////////////////////
    def trapezoidRule(function,a,b,n):
        
        # N is the number of trapezoids
        Δx = (b-a)/n
        Area = 0  
        
        for i in range(1,n+1):
        
            Area += (1/2)*Δx*( function( a+(i-1)*Δx ) + function( a+i*Δx ) )

        return(Area)
    #//////////////////////////////////////////////////////////////////////////////

    Integral_xCoordinates = [a]
    Integral_yCoordinates = [trapezoidRule(function,a,a,n)]
    function_xCoordinates = [a]
    function_yCoordinates = [function(a)]
    
    Δx = (b-a)/n
    
    for i in range(1,n+1):
        
        Integral_xCoordinates.append(Integral_xCoordinates[i-1] + Δx)
        Integral_yCoordinates.append(trapezoidRule(function,a,a+i*Δx,n))
        function_xCoordinates.append(function_xCoordinates[i-1] + Δx)
        function_yCoordinates.append(function(function_xCoordinates[i]))
        
    plt.plot(Integral_xCoordinates, Integral_yCoordinates, c = 'red', label ='F(x)')
    plt.plot(function_xCoordinates, function_yCoordinates, c = 'blue', label ='f(x)')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.legend()
    plt.show()
    
    CoordinateTable = array([Integral_xCoordinates,Integral_yCoordinates],float)
    return(transpose(CoordinateTable))
