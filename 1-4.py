import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
print(np_mat * 2)
print(np_mat + np.array([10, 10]))
np_mat2 = np.array(np_mat + np_mat)
print(np_mat2)