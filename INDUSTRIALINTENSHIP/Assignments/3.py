import numpy as np
M1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
M2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
M_add = np.add(M1, M2)
M_diff = np.subtract(M1, M2)
print("Matrix Addition:\n", M_add)
print("\nMatrix Subtraction:\n", M_diff)
