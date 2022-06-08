def square_matrix_simple(matrix=[]):
    result = []
    for each_row in matrix:
        each_matrix = map(lambda num: num**2, each_row)
        result.append(list(each_matrix))
    return result
