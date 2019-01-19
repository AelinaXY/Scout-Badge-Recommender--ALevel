#add references
array = [(1,0,0,1,1,0),(1,1,0,0,0,0),(1,0,0,0,0,0),(1,1,1,1,0,1)]

def func(a):
    s = sum(a)
    #new = []
    #for x in a:
        #new.append(x/(s**0.5))
    return [x/(s**0.5) for x in a]

for i in range(0,len(array)):
    print(func(array[i]))
