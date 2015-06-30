animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    total = 0
    largestKey = ''
    
    if aDict:
        for obj in aDict:
            count = 0
            if type(aDict[obj]) == list:
                for subobj in aDict[obj]:
                    count += 1
            else:
                count +=1
            
            if count >= total:
                total = count
                largestKey = obj
        
        return largestKey
            
    


    
    
    