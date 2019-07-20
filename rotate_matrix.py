def rotateMatrix(matrix):
    if (len(matrix) == 0 or len(matrix) != len(matrix[0])):
        return False

    n = len(matrix)
    layer_num = n//2
    #print(layer_num)

    for layer in range(layer_num):
       # print(layer)
        first = layer
        last = n - layer - 1
        offset = layer
        last_index = n - layer
        range_index = n - layer*2
        for index in range(first, last_index - 1):
            print('count')
            top = matrix[first][index]
            #print(first,index)
            # Top
            matrix[first][index] = matrix[last - index][first]
            print(last - index,first)
            # Left
            matrix[last - index][first] = matrix[last][last - index]

            # Bottom
            matrix[last][last - index] = matrix[index][last]

            # Right
            matrix[index][last] = top

    return matrix


matrix = [[1,2,3,4],[5,6,7,8],[0,2,4,6],[1,3,5,7]]
#matrix = [[1,2],[3,4]]
print(rotateMatrix(matrix))
