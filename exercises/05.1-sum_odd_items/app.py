arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds(list):
    odd = 0
    for i in list:
        if i % 2 != 0:
           odd += i 
    return odd

print(sumOdds(arr))

