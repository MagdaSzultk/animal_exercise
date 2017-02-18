import numpy
a =([[2,4], [1,1]])
b = ([94,35])
x =numpy.linalg.solve(a, b)
print('The numbers od chicken: ',int(x[0]), 'the numbers of rabbits: ',int(x[1]))