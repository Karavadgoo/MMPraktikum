import numpy as np


def get_max_before_zero(x):
    temp_arr = x[1:] - x[:-1]
    mask = temp_arr[temp_arr == x[1:]]
    return np.amax(mask) if mask.size else None


# x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
# print(x)
# print(get_max_before_zero(x))
# print()

# x = np.array([0, 7, 0, 3, 0])
# print(x)
# print(get_max_before_zero(x))
# print()

# x = np.array([6, 2, 3, 5, 7, 0])
# print(x)
# print(get_max_before_zero(x))
# print()

# x = np.array([0])
# print(x)
# print(get_max_before_zero(x))
# print()

# x = np.array([1, 1, 1, 1])
# print(x)
# print(get_max_before_zero(x))
# print()
