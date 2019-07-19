def compress(s):
    compressStr = ''
    countConsecutive = 0
    i = 0
    for i in range(len(s) - 1):
        countConsecutive += 1
        if (s[i] != s[i+1] or i == len(s) - 2):
            countStr = str(countConsecutive)
            countConsecutive = 0
            compressStr += s[i] + countStr

    if (len(s) == 0):
        return ''
    if (s[-1] == s[i] and len(compressStr)):
        compressStr = compressStr[:len(compressStr) - 1] + str(int(compressStr[len(compressStr) - 1]) + 1)
    else:
        compressStr += s[-1] + str(1)

    return compressStr

'''Test'''

s = 'aabbcdaae'
print(s)
print(compress(s))
s = 'aaaaabbbbb'
print(s)
print(compress(s))
s = '12481084ahfahfafjlajfljqrjuoiqrafafjljafjaf'
print(s)
print(compress(s))
s = 'a'
print(s)
print(compress(s))
s = ''
print(s)
print(compress(s))
