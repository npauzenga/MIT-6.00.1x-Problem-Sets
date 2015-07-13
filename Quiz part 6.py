def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    
    tests:
        L is empty
        new list is empty
        nothing is removed
        there is something other than string in list
    """
    try:
        for string in L:
            if not f(string):
                L.remove(string)
    except TypeError, e:
        return -1
    else:
        return len(L)
        
    
    
        
#run_satisfiesF(L, satisfiesF)

def f(s):
    if len(s) > 3:
        return True
    else:
        return False