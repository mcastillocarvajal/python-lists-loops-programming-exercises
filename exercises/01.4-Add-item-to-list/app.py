#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:

for i in range(0,10):
    my_list.append(random.randint(1,100))
    i += 1

print(my_list)
