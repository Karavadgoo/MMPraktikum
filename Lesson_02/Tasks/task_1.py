import numpy as np


def get_nonzero_diag_product(matrix):
    array_diagonal = matrix.diagonal()
    nonzero_diagonal = array_diagonal[array_diagonal != 0]
    return nonzero_diagonal.prod() if nonzero_diagonal.size else None


# Было:
# def get_nonzero_diag_product(matrix):
    # nonzero_diagonal = matrix.diagonal()[matrix.diagonal() != 0]
    # return nonzero_diagonal.prod() if nonzero_diagonal.size else None


# matrix = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
# print(matrix)
# print(np.diag(matrix))
# print(np.diag(matrix)[np.diag(matrix) != 0])
# print(get_nonzero_diag_product(matrix))
# print()

# matrix = np.array([[1, 2, 3, 4], [0, 0, 0, 4], [1, 2, 3, 4]])
# print(matrix)
# print(np.diag(matrix))
# print(np.diag(matrix)[np.diag(matrix) != 0])
# print(get_nonzero_diag_product(matrix))
# print()

# matrix = np.array([[1, 0, 1]])
# print(matrix)
# print(np.diag(matrix))
# print(np.diag(matrix)[np.diag(matrix) != 0])
# print(get_nonzero_diag_product(matrix))
# print()

# matrix = np.array([[0, 1, 1], [2, 0, 2], [3, 3, 0]])
# print(matrix)
# print(np.diag(matrix))
# print(np.diag(matrix)[np.diag(matrix) != 0])
# print(get_nonzero_diag_product(matrix))
# print()
