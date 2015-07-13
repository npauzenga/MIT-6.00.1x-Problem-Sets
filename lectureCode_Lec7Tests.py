def sumDigits(N):
    '''
    N: a non-negative integer
    ex: 126 = 6 + 2 + 1 = 9
    base case:
        N is one digit long so sum == N
    add last digit 
    '''    
    
    if N == 0:
        return 0
    else:
        return (N % 10) + sumDigits(N / 10)
        
#return sumDigits((N % 10) + ((N / 10) % 10))
# find last digit, remove it, add to total, find last digit, remove it.
# add to total...


def sumDigitsLoop(N):
    total = 0
    
    while N % 10 != N:
        total = total + (N % 10)
        N /= 10
    return total + N
    
     

        