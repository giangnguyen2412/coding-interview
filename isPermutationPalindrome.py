def buildCharFrequency(s):
    table = {}
    for c in s:
        if c not in table:
            table[c] = 1
        else:
            table[c] += 1
    return table

def checkMaxOneOdd(table):
    foundOdd = False
    for key,value in table.items():
        if value%2 == 1:
            if foundOdd:
                return False
            foundOdd = True

    return True

def isPermutationPalindrome_v1(s):
    table = buildCharFrequency(s)
    return checkMaxOneOdd(table)

def isPermutationPalindrome_v2(s):
    table  = {}
    countOdd = 0
    for c in s:
        if c not in table:
            table[c] = 1
        else:
            table[c] += 1

        if (table[c]%2 == 1):
            countOdd += 1
        else:
            countOdd -= 1

    return countOdd <= 1

def isPermutationPalindrome_v3(s):
    bitMap = 0
    max_char = ord('z')
    min_char = ord('a')  #Assuming s only contains 'z' to 'z' in ASCII, not Unicode

    for c in s:
        val_char = ord(c)
        shift = val_char - min_char
        bitMap ^= (1<<shift)

    print(bitMap)

    if bitMap == 0 or (bitMap-1)&bitMap == 0:
        return True
    else:
        return False

s1 = 'aby123098'
s2 = 'ayb390821189032yab'

result = isPermutationPalindrome_v1(s1)
print(result)
result = isPermutationPalindrome_v1(s2)
print(result)

result = isPermutationPalindrome_v2(s1)
print(result)
result = isPermutationPalindrome_v2(s2)
print(result)

s1 = 'abcmd'
s2 = 'asdflkjhglkjhgasdf'

result = isPermutationPalindrome_v3(s1)
print(result)
result = isPermutationPalindrome_v3(s2)
print(result)

s1 = 'qwertytyqwer'
s2 = 'asfpwtwtk'

result = isPermutationPalindrome_v3(s1)
print(result)
result = isPermutationPalindrome_v3(s2)
print(result)
