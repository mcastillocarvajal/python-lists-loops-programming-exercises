theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def func(i):
    if i == 1:
        return "wiki"
    else:
        return "woko"

result = list(map(func, theBools))
print(result)
