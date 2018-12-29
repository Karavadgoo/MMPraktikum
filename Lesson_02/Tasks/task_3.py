import numpy as np


def f(Z):
    isnan_column = np.isnan(Z)
    if np.all(isnan_column):
        Z = 0
    else:
        Z[isnan_column] = np.nanmean(Z)
    return Z


def replace_nan_to_means(X):
    Y = X.copy()
    return np.apply_along_axis(f, 0, Y)


# X = np.array([[1, 0, 1], [np.nan, 2, 5], [2, 0, np.nan], [3, 1, 3]])
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()

# X = np.array([[np.nan, 0, 1], [np.nan, 2, np.nan], [2, 0, np.nan], [3, 1, 3]])
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()

# X = np.array([[1, np.nan, 1], [np.nan, np.nan, 5], [2, np.nan, np.nan], [3, np.nan, 3]])
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()
