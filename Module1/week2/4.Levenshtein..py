def lever(token1, token2):
    rows = len(token1)+1
    cols = len(token2)+1
    matrix = [[0]*cols for _ in range(rows)]

    for i in range(cols):
        matrix[0][i] = i
    for i in range(rows):
        matrix[i][0] = i

    for i in range(1, rows):
        for j in range(1, cols):
            a = matrix[i-1][j]+1
            b = matrix[i][j-1]+1
            if token1[i-1] == token2[j-1]:
                c = matrix[i-1][j-1]
            else:
                c = matrix[i-1][j-1]+1

            matrix[i][j] = min(a, b, c)

    
    return min(a, b, c)


token1 = 'hi'
token2 = 'hello'
assert lever(token1, token2) == 4
print(lever('hola','hello'))
