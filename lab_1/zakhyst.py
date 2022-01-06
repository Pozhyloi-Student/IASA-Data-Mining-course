
#Варіант 1. Підгрупа 3. Захист 14:15

import numpy as np

array1 = np.arange(4)
print("array1 =", array1)
print("array1 + 10 =", np.add(array1, 10))
print("array1 - 10 =", np.subtract(array1, 10))
print("array1 * 3 =", np.multiply(array1, 3))
print("array1 / 2 =", np.divide(array1, 2))
print("array1 // 2 =", np.floor_divide(array1, 2))
 
print("-array1 = ", np.negative(array1))
print("arra1 ** 3 = ", np.power(array1, 3))
print("array1 % 2 = ", np.mod(array1, 2))

print("Abs(-array1) = ", abs(-array1))