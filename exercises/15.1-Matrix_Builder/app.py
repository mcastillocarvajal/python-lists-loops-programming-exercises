
import random

#Create the function below:

def matrixBuilder(num):
    matrix = []
    for i in range(num):
        row = []
        for col in range(num):
            row.append(1)
        matrix.append(row)
    return matrix

print (matrixBuilder(3))
