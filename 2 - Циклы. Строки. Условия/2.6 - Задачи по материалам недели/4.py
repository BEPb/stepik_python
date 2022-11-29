"""
Python 3.10 программа решения заданий курса stepik программирование на Python
Название файла 4.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-11-29
"""

'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк. После последней строки матрицы идёт строка, содержащая только строку "end" (без кавычек, см. Sample Input).

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

'''

str_input = str(input())

stop_word = "end"

if str_input != stop_word:
    matrix = [str_input.split()]

    # Ввод значений матрицы построчно, до строки "end":
    while str_input != stop_word:
        str_input = str(input())
        if str_input != stop_word and str_input != "":
            matrix.append(str_input.split())
        else:
            break

    # Глубокое копирование матрицы:
    matrix_copy = matrix[:]
    for n, m in enumerate(matrix):
        matrix_copy[n] = matrix[n][:]

    # Многомерный цикл:
    for i, ii in enumerate(matrix):
        for j, jj in enumerate(ii):

            len_str = len(matrix)
            len_col = len(ii)
            m_str_end = len_str - 1
            m_col_end = len_col - 1

            # Матрица 1х1:
            if len_str == 1 and len_col == 1:
                matrix_copy[i][j] = str(int(matrix[i][j]) * 4)

            # Квадратная или произвольная матрица:
            elif (len_str == len_col) or (len_str != len_col and len_str != 1 and len_col != 1):

                # First:
                if i == 0:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])

                    if j == 0:
                        left = int(matrix[i][m_col_end])
                        right = int(matrix[i][j + 1])

                    elif 0 < j < m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][j + 1])

                    elif j == m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][0])

                    matrix_copy[i][j] = str(up + down + left + right)

                # Mid:
                elif 0 < i < m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])

                    if j == 0:
                        left = int(matrix[i][m_col_end])
                        right = int(matrix[i][j + 1])

                    elif j < m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][j + 1])

                    elif j == m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][0])

                    matrix_copy[i][j] = str(up + down + left + right)

                # Last:
                elif i == m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])

                    if j == 0:
                        left = int(matrix[i][m_col_end])
                        right = int(matrix[i][j + 1])

                    elif 0 < j < m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][j + 1])

                    elif j == m_col_end:
                        left = int(matrix[i][j - 1])
                        right = int(matrix[i][0])

                    matrix_copy[i][j] = str(up + down + left + right)

            # Матрица со столбцом = 1:
            elif len_str > 1 and len_col == 1:
                left_right = int(matrix[i][j]) * 2

                if i == 0:
                    up = int(matrix[m_str_end][j])
                    down = int(matrix[i + 1][j])

                elif i == m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[0][j])

                elif 0 < i < m_str_end:
                    up = int(matrix[i - 1][j])
                    down = int(matrix[i + 1][j])

                matrix_copy[i][j] = str(up + down + left_right)

            # Матрица со строчкой = 1:
            elif len_str == 1 and len_col > 1:
                up_down = int(matrix[i][j]) * 2

                if j == 0:
                    left = int(matrix[i][m_col_end])
                    right = int(matrix[i][j + 1])

                elif j == m_col_end:
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][0])

                elif 0 < j < m_col_end:
                    left = int(matrix[i][j - 1])
                    right = int(matrix[i][j + 1])

                matrix_copy[i][j] = str(up_down + left + right)
            else:
                break

    # Вывод результата:
    if len(matrix_copy[:][:]) != 0:
        for z, zz in enumerate(matrix_copy):
            output_string = ""
            for x, xx in enumerate(zz):
                output_string += xx + " "
            print(output_string[:-1])
