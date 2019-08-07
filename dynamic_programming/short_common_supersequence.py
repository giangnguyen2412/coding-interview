# Using dp to solve this problem
# Given 2 strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences
def shortestCommonSuperSequence(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    if (str1_len == 0):
        return str2
    elif(str2_len == 0):
        return str1

    if (str1[-1] == str2[-1]):
        return shortestCommonSuperSequence(str1[:-1], str2[:-1]) + str1[-1]
    else:
        solution1 = shortestCommonSuperSequence(str1[:-1], str2)
        solution2 = shortestCommonSuperSequence(str1, str2[:-1])
        if len(solution1) < len(solution2):
            return shortestCommonSuperSequence(str1[:-1], str2) + str1[-1]
        else:
            return shortestCommonSuperSequence(str1, str2[:-1]) + str2[-1]

# Anyway. we can use memoization here to optimize the time complexity but increasing space compexity, its trivial so I will leave it!
str1 = "geek"
str2 = "eke"

print(shortestCommonSuperSequence(str1, str2))

str1 = "AGGTAB"
str2 = "GXTXAYB"

print(shortestCommonSuperSequence(str1, str2))
