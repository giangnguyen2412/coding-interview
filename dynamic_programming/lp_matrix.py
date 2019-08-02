def longestPathFromCell(i, j, matrix, n, cache):
    key = str(i) + str(j)

    if (key in cache):
        return cache[key]

    a = b = c = d = 1

    if (i < n -1):
        if (matrix[i+1][j] == matrix[i][j] + 1):
            a = 1 + longestPathFromCell(i+1, j, matrix, n, cache)

    if (j < n -1):
        if (matrix[i][j+1] == matrix[i][j] + 1):
            b =  1 + longestPathFromCell(i, j+1, matrix, n, cache)

    if (i > 0):
        if (matrix[i-1][j] == matrix[i][j] + 1):
            c = 1 + longestPathFromCell(i-1, j, matrix, n, cache)

    if (j > 0):
        if (matrix[i][j-1] == matrix[i][j] + 1):
            d = 1 + longestPathFromCell(i, j-1, matrix, n, cache)
    
    return max(a, b, c, d)

def longestPathOverMatrix(matrix, n, cache={}):
    max_len = 0

    for i in range(n):
        for j in range(n):
            key = str(i) + str(j)
            tmp_len = longestPathFromCell(i, j, matrix, n, cache)
            if (tmp_len > max_len):
                max_len = tmp_len
            cache[key] = tmp_len
    
    return max_len

matrix = [[1,2,9,10,20,10],[5,3,8,5,21,9],[4,6,7,1,22,8],[1,1,1,1,23,7],[4,4,4,4,24,6],[6,7,5,6,6,5]]
print(longestPathOverMatrix(matrix, 6))
