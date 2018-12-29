import math


def replace_nan_to_means(X):
    height, width = len(X), len(X[0])
    T = [[0] * height for _ in range(width)]
    for line in range(height):
        for col in range(width):
            T[col][line] = X[line][col]
    for i in range(width):
        nonnan_line = []
        summ = 0
        for j in range(height):
            if not math.isnan(T[i][j]):
                nonnan_line.append(T[i][j])
                summ += T[i][j]
        nonnans = len(nonnan_line)
        aver = summ / nonnans
        for j in range(height):
            if not nonnans:
                T[i] = [0] * height
                break
            elif math.isnan(T[i][j]):
                T[i][j] = aver
    Y = [[0] * width for _ in range(height)]
    for line in range(width):
        for col in range(height):
            Y[col][line] = T[line][col]
    return Y


# X = [[1, 0, 1], [math.nan, 2, 5], [2, 0, math.nan], [3, 1, 3]]
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()

# X = [[math.nan, 0, 1], [math.nan, 2, math.nan], [2, 0, math.nan], [3, 1, 3]]
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()

# X = [[1, math.nan, 1], [math.nan, math.nan, 5], [2, math.nan, math.nan], [3, math.nan, 3]]
# print()
# print(X)
# print(replace_nan_to_means(X))
# print(X)
# print()
