import numpy as np


def encode_rle(x):
    dif_elem_indexes = np.nonzero(x - np.append(np.array([np.nan]), x[:-1]))[0]
    numbers = x[dif_elem_indexes]
    lengths = np.append(dif_elem_indexes[1:], [x.shape[0]]) - dif_elem_indexes
    return (numbers, lengths)


# x = np.array([2, 2, 2, 3, 3, 3, 5, 3])
# print(x)
# print(encode_rle(x))
# print()

# x = np.array([1, 2, 3, 4, 5])
# print(x)
# print(encode_rle(x))
# print()

# x = np.array([7, 7, 7, 7, 7, 7, 7])
# print(x)
# print(encode_rle(x))
# print()
