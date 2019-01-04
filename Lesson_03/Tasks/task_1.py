import numpy as np


class CooSparseMatrix:
    def __init__(self, original_matrix, shape=None):
        self.shape = original_matrix.shape
        self.height = self.shape[0]
        self.width = self.shape[1]
        if shape is None or shape == self.shape:
            nonzeros = original_matrix[original_matrix != 0]
            nonzeros_indices = np.nonzero(original_matrix)
            self.matrix = np.array(list(zip(nonzeros, 
                                            nonzeros_indices[0], 
                                            nonzeros_indices[1])), dtype=float)
            # Интересно, а могли бы мы здесь написать self = np.array(...), 
            # и почему так не делают...
            # После тестов написал мне: "__init__() should return None, not 'numpy.ndarray'", 
            # вот почему мне пришлось убрать return self.matrix...
            # 
            # Обидно также, что np.array() не кушает сразу результат ф-ии zip
            # 
            # Мне бы хотелось иметь np.array с первым столбцом из float и 
            # остальными из int. И я даже знаю как это сделать, но потом надо
            # усложнять и другие методы, поэтому я на это забил и где нужно
            # превращаю второй и третий столбец в int-ы
        else:
            raise TypeError('Wrong shape')


    def add_element(self, value, coords):
        if (coords[0] not in range(self.height) or 
            coords[1] not in range(self.width)):
            raise TypeError('Coordinates are out of the size of the matrix')
        elif coords in set(zip(self.matrix[:, 1], self.matrix[:, 2])):
            raise TypeError('Element with the same coordinates already exists')
        else:
            self.matrix = np.append(self.matrix, 
                                    np.array((value,) + coords, ndmin=2), axis=0)


    def __add__(self, coo_matrix):
        if self.shape == coo_matrix.shape:
            return CooSparseMatrix(self.toarray() + coo_matrix.toarray())
        else:
            raise TypeError('Shapes of the matrices must be equal')


    def __mul__(self, value):
        # Мне не захотелось определять метод copy(), поэтому вместо new_matrix = self.copy(),
        # мы имеем следующую странную, но непротиворечивую конструкцию:
        new_matrix = CooSparseMatrix(np.zeros((self.height, self.width)))
        new_matrix.matrix = np.hstack((self.matrix[:, 0].reshape(-1, 1) * value, 
                                       self.matrix[:, 1:]))
        return new_matrix
    
    def __getitem__(self, i):
        # Я предположил, что используется нумерация строк с 1-го до n...
        if i in range(1, self.height + 1):
            return self.toarray()[i - 1]
        else:
            raise TypeError('Row', i, 'is out of the size of the matrix')


    def toarray(self):
        output_matrix = np.zeros((self.height, self.width))
        output_matrix[(self.matrix[:, 1].astype(int)), 
                      (self.matrix[:, 2].astype(int))] = self.matrix[:, 0]
        return output_matrix


first_matrix = np.array([[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 0, 3]])
print(first_matrix)
print()
a = CooSparseMatrix(first_matrix, (3, 4))
print(a.matrix)
print()
# Проверяем работоспособность shape == None
print(CooSparseMatrix(first_matrix).matrix)
print()
# Проверяем конструктор на нулевой матрице
second_matrix = np.zeros((5, 5))
print(second_matrix)
print()
b = CooSparseMatrix(second_matrix)
print(b.matrix)
print()
# Опциональная проверка на неправильный shape
# print(CooSparseMatrix(first_matrix, (9, 9)))
# print()

print(first_matrix)
print()
print(a.matrix)
print()
a.add_element(5.5, (0, 3))
print(a.matrix)
print()
# Опциональная проверка на попытку перезаписи элемента
# a.add_element(5.5, (1, 1))
# print(a)
# print()
# Опциональная проверка на запись элемента с неверными координатами
# a.add_element(5.5, (5, 5))
# print(a.matrix)
# print()

third_matrix = np.array([[0, 0, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0]])
fourth_matrix = np.ones((3, 5))
c, d = CooSparseMatrix(third_matrix), CooSparseMatrix(fourth_matrix)
print(third_matrix)
print()
print(c.matrix)
print()
print(fourth_matrix)
print()
print(d.matrix)
print()
print((c + d).matrix)
print()
# Проверяем, что испытуемый метод не меняет исходных матриц 
print(c.matrix)
print()
print(d.matrix)
print()
# Опциональная проверка на сложение матриц с разными shape
# print((CooSparseMatrix(np.ones((3, 5))) + CooSparseMatrix(np.zeros((5, 3)))).matrix)

print(a.toarray())
print()
print(a.matrix)
print()
print((a * 2.5).matrix)
print()
# Проверяем, что испытуемый метод не меняет исходных матрицу
print(a.matrix)
print()

print(a.toarray())
print()
print(a.matrix)
print()
print(a[2])
print()
# Опциональная проверка на допустимость значения i
# print(a[0])
# print()

print(a.toarray())
print()
print(a.matrix)
print()
print(a.toarray())
print()
