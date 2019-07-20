def oneEditAway(first, second):
    if (len(first) ==  len(second)):
        return oneEditReplace(first, second)
    elif (len(first) + 1 == len(second)):
        return oneEditInsert(first, second)
    elif (len(first) - 1 == len(second)):
        return oneEditInsert(second, first)
    else:
        return False

def oneEditReplace(first, second):
    foundDifference = False
    for i in range(len(first)):
        if (first[i] != second[i]):
            if (foundDifference == True):
                return False
            foundDifference = True
    return True

def oneEditInsert(first, second):
    idx1 = 0
    idx2 = 0
    while (idx1 < len(first) and idx2 < len(second)):
        if (first[idx1] != second[idx2]):
            if (idx1 != idx2):
                return False
            idx2 += 1
        else:
            idx1 += 1
            idx2 += 1

    return True

print(oneEditAway('pale','ple'))
print(oneEditAway('pales', 'pale'))
print(oneEditAway('pale', 'bale'))
print(oneEditAway('pale', 'bae'))
