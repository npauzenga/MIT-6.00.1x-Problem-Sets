def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 2
    
    if b**power >= x:
        return power
    else:
        return myLog(x, b**(power + 1))
        