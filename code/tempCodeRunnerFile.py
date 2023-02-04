matrix_norm = matrix.subtract(matrix.mean(axis=1), axis = 'rows')
    matrix_norm.head()
    matrix_norm.to_csv('ressources/test.csv')