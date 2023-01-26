def max(a,b):
    #if a > b:
        #return a
    
    #else:
        #return b
    return a if a>b else b
    
biggest = (lambda a,b: a if a>b else b)(8,5)
print(biggest)
