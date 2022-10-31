import numpy as np

A = [int(i) for i in input("Value of Vector A: ").split(',')]
B = [int(i) for i in input("Value of Vector B: ").split(',')]

crossProduct = np.cross(A, B)

print(crossProduct)
