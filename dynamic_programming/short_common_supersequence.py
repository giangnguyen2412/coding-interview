# Using dp to solve this problem
# Given 2 strings str1 and str2, find the len of shortest string that has both str1 and str2 as subsequences
def shortestCommonSuperSequenceLen(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    if (str1_len == 0):
        return str2_len
    elif(str2_len == 0):
        return str1_len

    if (str1[-1] == str2[-1]):
        return 1 + shortestCommonSuperSequenceLen(str1[:-1], str2[:-1])
    else:
        return 1 + min(shortestCommonSuperSequenceLen(str1[:-1], str2), shortestCommonSuperSequenceLen(str1, str2[:-1]))

str1 = "geek"
str2 = "eke"

print(shortestCommonSuperSequenceLen(str1, str2))

str1 = "AGGTAB"
str2 = "GXTXAYB"

print(shortestCommonSuperSequenceLen(str1, str2))
