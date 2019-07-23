def lcs(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    lcs_solution = []
    lcs_cnt = 0

    if (s1_len == 0 or s2_len == 0):
        return 0

    while (s1_len > 0 and s2_len > 0):
        if (s1[s1_len - 1] == s2[s2_len - 1]):
            lcs_solution.append(s1[s1_len - 1])
            lcs_cnt += 1

            s1_len -= 1
            s2_len -= 1
        else:
            lcs_cnt += max(lcs(s1[:s1_len - 1], s2[:s2_len]), lcs(s1[:s1_len], s2[:s2_len - 1]))
            break
    
    return lcs_cnt

s1 = 'ABCDGH'
s2 = 'AEDFHR'
print(s1, s2, lcs(s1, s2))

s1 = 'AAAAA'
s2 = 'AAABA'
print(s1, s2, lcs(s1, s2))

s1 = ''
s2 = ''
print(s1, s2, lcs(s1, s2))

s1 = 'A'
s2 = 'A'
print(s1, s2, lcs(s1, s2))

s1 = 'AB'
s2 = 'BA'
print(s1, s2, lcs(s1, s2))

s1 = 'ASDG'
s2 = 'QWER'
print(s1, s2, lcs(s1, s2))

s1 = 'ASDGHJKL'
s2 = 'ASDQWEbGBHNJKMLL'
print(s1, s2, lcs(s1, s2))

