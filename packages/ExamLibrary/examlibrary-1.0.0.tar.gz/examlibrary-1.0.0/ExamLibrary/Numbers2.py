#Библиотека NumPy (Numerical Python) - это одна из основных библиотек для работы с массивами и матрицами в Python.
# NumPy предоставляет множество функций и операций для эффективной работы с числовыми данными.

#np.array([[]])-создание матрицы
#linalg-линейная алгебра
#np.linalg.det()-нахождение детерминанта(определителя матрицы)
#np.round()-округление
#np.linalg.matrix_rank()-нахождение ранга матрицы
#np.linalg.inv()-транспортирование матрицы
#np.dot(A, B)-перемножение матриц
#np.add(A, B)-сложение матриц
import numpy as np
def number21():
    A = np.array([[1, -2, 0], [0, 1, 3], [1, 0, -1]])
    B = np.array([3, 15, 5])
    detA = np.linalg.det(A)
    Ax = A.copy()
    Ay = A.copy()
    Az = A.copy()
    Ax[:, 0] = B
    Ay[:, 1] = B
    Az[:, 2] = B
    detAx = np.linalg.det(Ax)
    detAy = np.linalg.det(Ay)
    detAz = np.linalg.det(Az)
    x = np.round(detAx / detA)
    y = np.round(detAy / detA)
    z = np.round(detAz / detA)
    print(x)
    print(y)
    print(z)

def number22():
    A1 = np.array([[1, 2, -1], [3, 0 , -2], [4, -3, 5]])
    B1 = np.array([[2, 6, 8], [-5, -7, -4], [0, 1, -2]])
    summa = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    for i in range(len(A1)):
        for j in range(len(B1)):
            summa[i][j] = A1[i][j]+B1[i][j]
    detsumma = np.round(np.linalg.det(summa))
    print(detsumma)

def number23():
    A4 = np.array([[2, 5], [4, 10]])
    B4 = np.array([[3, 6]])
    detA4 = np.linalg.det(A4)
    Ax4 = A4.copy()
    Ay4 = A4.copy()
    Ax4[:, 0] = B4
    Ay4[:, 1] = B4
    detAx4 = np.linalg.det(Ax4)
    detAy4 = np.linalg.det(Ay4)
    if detA4 == 0 and detAx4 == 0 and detAy4 == 0:
        print("имеет множество решений")

def number24():
    A5 = np.array([[3, -5], [6, -10]])
    B5 = np.array([[7, -1]])
    detA5 = np.linalg.det(A5)
    Ax5 = A5.copy()
    Ay5 = A5.copy()
    Ax5[:, 0] = B5
    Ay5[:, 1] = B5
    detAx5 = np.linalg.det(Ax5)
    detAy5 = np.linalg.det(Ay5)
    if detA5 == 0 and detAx5 != 0 or detAy5 != 0:
        print("не имеет решений")

def number25():
    def create_matrix(rows, cols):
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = input(f'Введите элемент матрицы [{i + 1}][{j + 1}]: ')
                row.append(int(value))
            matrix.append(row)
        return matrix

    rows = int(input('Введите количество строк: '))
    cols = int(input('Введите количество столбцов: '))

    matrix = create_matrix(rows, cols)
    print('Ваша матрица:')
    for row in matrix:
        print(row)
    r = np.linalg.matrix_rank(matrix)
    print(f'Ранг матрицы равен: {r}')

def number26():
    A3 = np.array([[2, 3], [-5, 6]])
    B3 = np.array([4, 17])
    transA3 = np.linalg.inv(A3)
    X = np.dot(transA3, B3)
    print(X)

def number27():
    A2 = np.array([[2, 1, 0], [3, 1, 1]])
    B2 = np.array([[1, 2], [2, 1], [2, 2]])
    multiplication = np.array([[0, 0], [0, 0]])
    for i in range(len(A2)):
        for j in range(len(B2[0])):
            for k in range(len(B2)): multiplication[i][j] += A2[i][k] * B2[k][j]
    print(multiplication)

def number28():
    detmatrix = np.array([[-1, 2, 3], [2, 0, -3], [3, 2, 5]])
    def algebraic_cofactor(matrix, i, j):
        minor_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
        cofactor = (-1) ** (i + j) * np.linalg.det(minor_matrix)
        return cofactor
    a13 = algebraic_cofactor(detmatrix, 0, 2)
    a21 = algebraic_cofactor(detmatrix, 1, 0)
    a31 = algebraic_cofactor(detmatrix, 2, 0)
    print(a13)
    print(a21)
    print(a31)
    #В функции algebraic_cofactor используется функция np.delete(),
    # которая удаляет элементы из массива по указанной оси axis.

    #В NumPy массив с n-мерами может иметь несколько осей (axis).
    # Ось axis=0 соответствует строкам, а ось axis=1 соответствует столбцам.
    # При удалении элементов из массива с помощью np.delete(), параметр axis указывает,
    # по какой оси производится удаление.

    #В данном случае, в функции algebraic_cofactor используется np.delete(matrix, i, axis=0),
    # что означает удаление строки с индексом i из матрицы matrix,
    # а затем используется еще один вызов np.delete()
    # с axis=1 для удаления столбца с индексом j из этой "уменьшенной" матрицы.

    #Таким образом, параметр axis в функции np.delete()
    # указывает, по какой оси производить удаление (столбцы или строки).