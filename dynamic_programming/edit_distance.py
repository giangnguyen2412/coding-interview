import timeit

def editDistance(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    # Add all letter of str2
    if (str1_len == 0):
        return str2_len

    # Remove all letters in str1
    if (str2_len == 0):
        return str1_len

    # Last letter is same, just ignore it
    if (str1[str1_len - 1] == str2[str2_len -1]):
        return editDistance(str1[:str1_len - 1], str2[:str2_len -1])

    return (1 + min(editDistance(str1, str2[:str2_len - 1]), # Insert to str1
                    editDistance(str1[: str1_len -1], str2), # Remove
                    editDistance(str1[: str1_len -1], str2[: str2_len - 1]))) # Replace

def editDistance_memoize(str1, str2, dct={}):
    if (str1 + ',' + str2) in dct:
        return dct[(str1 + ',' + str2)]
        
    str1_len = len(str1)
    str2_len = len(str2)

    # Add all letter of str2
    if (str1_len == 0):
        return str2_len

    # Remove all letters in str1
    if (str2_len == 0):
        return str1_len

    # Last letter is same, just ignore it
    if (str1[str1_len - 1] == str2[str2_len -1]):
        return editDistance_memoize(str1[:str1_len - 1], str2[:str2_len -1], dct)

    
    ins_cost = editDistance_memoize(str1, str2[:str2_len - 1], dct)
    rem_cost = editDistance_memoize(str1[: str1_len -1], str2, dct)
    rep_cost = editDistance_memoize(str1[: str1_len -1], str2[: str2_len - 1], dct)
    if (str1 + ',' + str2[:str2_len - 1]) not in dct:
        dct[(str1 + ',' + str2[:str2_len - 1])] = ins_cost

    if (str1[: str1_len -1] + ',' + str2) not in dct:
        dct[(str1[: str1_len -1] + ',' + str2)] = rem_cost

    if (str1[: str1_len -1] + ',' + str2[: str2_len - 1]) not in dct:
        dct[(str1[: str1_len -1] + ',' + str2[: str2_len - 1])] = rep_cost

    return 1 + min(ins_cost, rem_cost, rep_cost)


def editDistance_bottomup(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    dp = [[0 for i in range(str2_len + 1)] for j in range(str1_len + 1)]
    
    for i in range(str1_len + 1):
        for j in range(str2_len + 1):
            if (i == 0):
                dp[i][j] = j

            elif (j == 0):
                dp[i][j] = i

            elif (str1[i - 1] == str2[j - 1]):
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[str1_len][str2_len]





start = timeit.default_timer()
str1 = 'geek'
str2 = 'gesek'
print(editDistance(str1, str2))

str1 = 'aafalfjas'
str2 = 'qjf;lk'
print(editDistance(str1, str2))

str1 = 'sunday'
str2 = 'saturday'
print(editDistance(str1, str2))
stop = timeit.default_timer()
print('Elapsed time naive:', stop - start)

start = timeit.default_timer()
str1 = 'geek'
str2 = 'gesek'
print(editDistance_memoize(str1, str2))

str1 = 'aafalfjas'
str2 = 'qjf;lk'
print(editDistance_memoize(str1, str2))

str1 = 'sunday'
str2 = 'saturday'
print(editDistance_memoize(str1, str2))
stop = timeit.default_timer()
print('Elapsed time naive:', stop - start)

start = timeit.default_timer()
str1 = 'geek'
str2 = 'gesek'
print(editDistance_bottomup(str1, str2))

str1 = 'aafalfjas'
str2 = 'qjf;lk'
print(editDistance_bottomup(str1, str2))

str1 = 'sunday'
str2 = 'saturday'
print(editDistance_bottomup(str1, str2))
stop = timeit.default_timer()
print('Elapsed time tabulate:', stop - start)
