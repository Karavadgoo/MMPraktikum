import numpy as np


def replace_nan_to_means(X):
    Y = X.copy()
    isnan_array = np.isnan(X)
    nanmean_array = np.nanmean(X, axis=0)
    nanmean_array[np.isnan(nanmean_array)] = 0
    Y[isnan_array] = (nanmean_array + np.zeros(X.shape))[isnan_array]
    return Y


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
