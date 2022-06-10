def generator():
    for i in range(10):
        if (i % 2 == 0 ):
            yield i
#Function call using for loop
for i in generator():
    print(i)   
    
    
#ex:
def multiple_yeild():
    a1 = "Neeti"
    yield a1
    
    a2 = "Srabonti"
    yield a2
    
    a3 = "Azimpur"
    yield a3
    
multiobj = multiple_yeild()
print(next(multiobj))
print(next(multiobj))
print(next(multiobj))
