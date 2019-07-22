def isSubString(s1, s2):
    if s1 in s2:
        return True
    else:
        return False

def isRotation(s1, s2):
    s1_tmp = s1 + s1
    if (len(s1) != len(s2)):
        print("The len of two strings are not the same!")
        return False

    if (isSubString(s2, s1_tmp)):
        return True
    else:
        return False

s1 = 'conmeoden'
s2 = 'denconmeo'

print(isRotation(s1,s2))

s1 = 'conmeodena'
s2 = 'denconmeo'

print(isRotation(s1,s2))


s1 = 'conmeoden'
s2 = 'danconmeo'

print(isRotation(s1,s2))

