import math
import timeit

def uglyNumber_tabulation(n):
	ugly_list = [0]*n
	ugly_list[0] = 1
	
	ugly_2 = 2
	ugly_2_cnt = 1
	ugly_3 = 3
	ugly_3_cnt = 1
	ugly_5 = 5
	ugly_5_cnt = 1
	
	for i in range(1, n):
		ugly_list[i] = min(ugly_2, ugly_3, ugly_5)
		
		if (ugly_list[i] == ugly_2):
			ugly_2 = 2*ugly_list[ugly_2_cnt]
			ugly_2_cnt +=1 
		elif (ugly_list[i] == ugly_3):
			ugly_3 = 3*ugly_list[ugly_3_cnt]
			ugly_3_cnt += 1
		else:
			ugly_5 = 5*ugly_list[ugly_5_cnt]
			ugly_5_cnt += 1
			
	return ugly_list[-1]
	

def rewrite_dp(n):
	ugly = [0]*n
	ugly[0] = 1

	i2 = i3 = i5 = 0

	next_2 = 2
	next_3 = 3
	next_5 = 5

	for i in range(1, n):
		ugly[i] = min (next_2, next_3, next_5)

		if (ugly[i] == next_2):
			i2 += 1
			next_2 = 2*ugly[i2]
		if (ugly[i] == next_3):
			i3 += 1
			next_3 = 3*ugly[i3]
		if (ugly[i] == next_5):
			i5 += 1
			next_5 = 5*ugly[i5]

	return ugly[-1]
			
	

# Python program to find n'th Ugly number 

# Function to get the nth ugly number 
def getNthUglyNo_Sol2(n): 

	ugly = [0] * n # To store ugly numbers 

	# 1 is the first ugly number 
	ugly[0] = 1

	# i2, i3, i5 will indicate indices for 2,3,5 respectively 
	i2 = i3 =i5 = 0

	# set initial multiple value 
	next_multiple_of_2 = 2
	next_multiple_of_3 = 3
	next_multiple_of_5 = 5

	# start loop to find value from ugly[1] to ugly[n] 
	for l in range(1, n): 

		# choose the min value of all available multiples 
		ugly[l] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) 

		# increment the value of index accordingly 
		if ugly[l] == next_multiple_of_2: 
			i2 += 1
			next_multiple_of_2 = ugly[i2] * 2

		if ugly[l] == next_multiple_of_3: 
			i3 += 1
			next_multiple_of_3 = ugly[i3] * 3

		if ugly[l] == next_multiple_of_5: 
			i5 += 1
			next_multiple_of_5 = ugly[i5] * 5

	# return ugly[n] value 
	return ugly[-1] 

start = timeit.default_timer()
# Driver code to test above functions 
no = getNthUglyNo_Sol2(70) 
print("70th ugly no. is ", no) 

stop = timeit.default_timer()

#print('Eslaped Time Sol2: ', stop - start)

start = timeit.default_timer()
# Driver code to test above functions 
no = uglyNumber_tabulation(70) 
print("70th TABULATION ugly no. is ", no) 

stop = timeit.default_timer()

#print('Eslaped Time Sol2: ', stop - start)


# Python3 code to find nth ugly number 

# This function divides a by greatest 
# divisible power of b 
def maxDivide( a, b ): 
	while a % b == 0: 
		a = a / b 
	return a 

# Function to check if a number 
# is ugly or not 
def isUgly( no ): 
	no = maxDivide(no, 2) 
	no = maxDivide(no, 3) 
	no = maxDivide(no, 5) 
	return 1 if no == 1 else 0

# Function to get the nth ugly number 
def getNthUglyNo( n ): 
	i = 1
	count = 1 # ugly number count 

	# Check for all integers untill 
	# ugly count becomes n 
	while n > count: 
		i += 1
		if isUgly(i): 
			count += 1
	return i 

start = timeit.default_timer()
# Driver code to test above functions 
no = getNthUglyNo(70) 
print("70th ugly no. is ", no) 

stop = timeit.default_timer()

#print('Eslaped Time Sol1: ', stop - start)

# This code is contributed by "Sharad_Bhardwaj". 


def checkUglyNumber(n):
    if (n%2 and n%3 and n%5):
        return False
    if (n == 2 or n == 3 or n == 5):
        return True
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if (n%2 == 0):
            return checkUglyNumber(n/2)
        elif (n%3 == 0):
            return checkUglyNumber(n/3)
        elif (n%5 == 0):
            return checkUglyNumber(n/5)

    return True

def uglyNumber(n):
    i = 1
    ugly_num = 1
    while(1):
        i += 1
        if True == checkUglyNumber(i):
            ugly_num += 1
        if (ugly_num == n):
            return i

def checkUglyNumber_memoize(n, cache):
    if (n in cache):
        return cache[n]

    if (n%2 and n%3 and n%5):
        return False
    if (n == 2 or n == 3 or n == 5):
        return True
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if (n%2 == 0):
            return checkUglyNumber_memoize(n/2, cache)
        elif (n%3 == 0):
            return checkUglyNumber_memoize(n/3, cache)
        elif (n%5 == 0):
            return checkUglyNumber_memoize(n/5, cache)

    return True

def uglyNumber_memoize(n, cache = {}):
    i = 1
    ugly_num = 1
    while(1):
        i += 1
        if True == checkUglyNumber_memoize(i, cache):
            ugly_num += 1
            cache[i] = True
        else:
            cache[i] = False

        if (ugly_num == n):
            return i

start = timeit.default_timer()

n = 70
print(uglyNumber(n))
#n = 1000   
#print(uglyNumber(n))
#n = 1500   
#print(uglyNumber(n))
#n = 15000   
#print(uglyNumber(n))

stop = timeit.default_timer()

print('Eslaped Time: ', stop - start)

start = timeit.default_timer()

n = 70
print(uglyNumber_memoize(n))
#n = 1000   
#print(uglyNumber_memoize(n))
#n = 1500   
#print(uglyNumber_memoize(n))
#n = 15000   
#print(uglyNumber_memoize(n))

stop = timeit.default_timer()

print('Eslaped Time for memoize: ', stop - start)


start = timeit.default_timer()

n = 70
print(rewrite_dp(n))
#n = 1000   
#print(rewrite_dp(n))
#n = 1500   
#print(rewrite_dp(n))
#n = 15000   
#print(rewrite_dp(n))

stop = timeit.default_timer()

print('Eslaped Time for rewrite dp: ', stop - start)
