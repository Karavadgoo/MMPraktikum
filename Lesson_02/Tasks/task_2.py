import numpy as np


def get_elements_by_indexes(X, i_indexes, j_indexes):
    return X[i_indexes, j_indexes]


# X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
# i_indexes = np.array([1, 2])
# j_indexes = np.array([2, 2])
# print(X, i_indexes, j_indexes, sep='\n')
# print(get_elements_by_indexes(X, i_indexes, j_indexes))
# print()

# X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
# i_indexes = np.array([1, 2, 3])
# j_indexes = np.array([2, 2, 0])
# print(X, i_indexes, j_indexes, sep='\n')
# print(get_elements_by_indexes(X, i_indexes, j_indexes))
# print()

# X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
# i_indexes = np.array([1, 1, 1])
# j_indexes = np.array([1, 1, 1])
# print(X, i_indexes, j_indexes, sep='\n')
# print(get_elements_by_indexes(X, i_indexes, j_indexes))
# print()
