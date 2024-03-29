# longest increasing subsequence

import timeit

# global variable to store the maximum 
global maximum 
  
def _lis(arr , n ): 
  
    # to allow the access of global variable 
    global maximum 
  
    # Base Case 
    if n == 1 : 
        return 1
  
    # maxEndingHere is the length of LIS ending with arr[n-1] 
    maxEndingHere = 1
  
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
       IF arr[n-1] is maller than arr[n-1], and max ending with 
       arr[n-1] needs to be updated, then update it"""
    for i in range(1, n): 
        res = _lis(arr , i) 
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere: 
            maxEndingHere = res +1
  
    # Compare maxEndingHere with overall maximum. And 
    # update the overall maximum if needed 
    maximum = max(maximum , maxEndingHere) 
  
    return maxEndingHere 
  
def lis_naive(arr): 
  
    # to allow the access of global variable 
    global maximum 
  
    # lenght of arr 
    n = len(arr) 
  
    # maximum variable holds the result 
    maximum = 1
  
    # The function _lis() stores its result in maximum 
    _lis(arr , n) 
  
    return maximum 

def lis(arr):
    dct = {}
    arr_len = len(arr)

    lis = [1]*arr_len

    for i in range(1, arr_len):
        for j in range(0 , i):
            if (arr[i] > arr[j]) and (lis[i] < lis[j] + 1):
                lis[i] = lis[j] + 1

    return max(lis), dct


def lis_recursive(arr):
    ret = 1 # default return value 
    arr_len = len(arr)
    if (arr_len <= 1):
        return arr_len

    index1 = arr_len - 1
    while (index1 > 0):
        index2 = index1 - 1
        while (index2 >= 0):
            if (arr[index1] > arr[index2]):
                return 1 + lis_recursive(arr[:index2 + 1])
            
            index2 -= 1
        index1 -= 1
    return ret

def lis_recursive_memoize(arr, dct={}):
    ret = 1 # default return value 
    arr_len = len(arr)
    if (arr_len <= 1):
        return arr_len

    index1 = arr_len - 1
    while (index1 > 0):
        if index1 in dct:
            return dct[index1]
        index2 = index1 - 1
        while (index2 >= 0):
            if (arr[index1] > arr[index2]):
                lis_cnt = 1 + lis_recursive_memoize(arr[:index2 + 1], dct)
                dct[index1] = lis_cnt
                return lis_cnt
            
            index2 -= 1
        index1 -= 1
    return ret


start = timeit.default_timer()
arr = [2, 3, 1, 4, 6]
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
arr = [3, 10, 2, 1, 20]
arr = [3, 2]
arr = [9, 8, 6, 5, 5, 3, 2, 1, 1, 0]
arr = [50, 3, 10, 7, 40, 80, 90, 91, 92, 93, 94, 95, 96, 97, 1000]
print(lis_recursive(arr))
stop = timeit.default_timer()
print('Elapsed time recursion: {}'.format(stop - start))

start = timeit.default_timer()
print(lis_recursive_memoize(arr))
stop = timeit.default_timer()
print('Elapsed time recursion memoize: {}'.format(stop - start))

'''
start = timeit.default_timer()
#arr = [3, 10, 2, 1, 20]
#arr = [50,3,10,7,40,80]
arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
cnt, dct = lis(arr)
print(cnt)

tmp_list = []
for i in range(len(arr)):
    val1 = arr[i]
    tmp_list.append(val1)
    for j in range(i+1, len(arr)):
        val2 = arr[j]
        if val2 > val1:
            tmp_list.append(val2)
            val1 = arr[j]
    if (len(tmp_list) == cnt):
        print(tmp_list)
        break
    tmp_list = []


stop = timeit.default_timer()

print('Eslaped Time dp: ', stop - start)

start = timeit.default_timer()
arr = [50,3,10,7,40,80]
print(lis_naive(arr))
stop = timeit.default_timer()

print('Eslaped Time naive: ', stop - start)

arr = [5,7,3,4,10]
arr = [3,10,2,1,20]
arr = [3,2]
#arr = [50,3,10,7,40,80]
#print(lis(arr))
'''
