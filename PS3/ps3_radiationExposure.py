'''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
'''
def f(x):
	import math
	return 10*math.e**(math.log(0.5)/5.27 * x)
'''
    Int Int Float -> Float
    purpose: computes radiation exposed to between start and stop times,
            using step
    Examples:
        >>> radiationExposure(0, 5, 1)
            39.10318784326239
        >>> radiationExposure(5, 11, 1)
            22.94241041057671
        >>> radiationExposure(0, 11, 1)
            62.0455982538
'''

#def radiationExposure(start, stop, step):
#    (... start stop step)
    
def radiationExposure(start, stop, step):
    radiation = 0.0
    i = start
    
    while i < stop:
        radiation += f(i) * step
        print i, radiation
        i += step
        
    return radiation

def radiationForLoop(start, stop, step):
    radiation = 0.0
    
    for i in range(start, stop, step):
        radiation += f(i)
        print radiation
    return radiation
    
     
   
    
    
    
