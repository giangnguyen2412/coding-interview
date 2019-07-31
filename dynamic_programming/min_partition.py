def findMinRec(arr, arr_len, calculated_sum, total_sum):
    if (arr_len == 0):
        return abs((total_sum - calculated_sum) - calculated_sum)

    dct = min(findMinRec(arr, arr_len - 1, calculated_sum + arr[arr_len - 1], total_sum),
                findMinRec(arr, arr_len - 1, calculated_sum, total_sum))
    return dct

def minPartition(arr):
    arr_len = len(arr)
    total_sum = sum(arr)

    return findMinRec(arr, arr_len, 0, total_sum)



       

#arr = [5,1,4,3,4,1,5,6,7,8,2,5,2,6,1,7,8,77,44,88,44,44,11,4,1,5,6,7,8,2,5,2,6,1,7,8,77,44,88,44,44,11]
#print(sum(arr))
arr = [1,6,11,5]

print(minPartition(arr))
        
