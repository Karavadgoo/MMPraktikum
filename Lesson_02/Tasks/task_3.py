import numpy as np


def replace_nan_to_means(X):
    Y = X.copy()

    def f(Z):
        if np.all(np.isnan(Z)):
            Z[np.isnan(Z)] = 0
        else:
            Z[np.isnan(Z)] = np.nanmean(Z)
        # try:
            # Z[np.isnan(Z)] = np.nanmean(Z)
        # except Exception:
            # Z[np.isnan(Z)] = 0
        return Z
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
