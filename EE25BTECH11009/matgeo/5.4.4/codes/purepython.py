import numpy as np
a = np.array([[2, 4],
              [-1, 2]])
inverse_a = np.array([[1/3, -2/3],
                      [1/6, 1/3]])
b = a @ inverse_a
print(b)