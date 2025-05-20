def encodeString(stringVal):
    encodedList = []
    prev_char = stringVal[0]
    count = 0

    for char in stringVal:
        if prev_char != char:
            encodedList.append((prev_char, count))
            count = 0
        prev_char = char
        count += 1

    encodedList.append((prev_char, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        decodedStr = decodedStr + item[0] * item[1]
    return decodedStr

print(encodeString('AAAAABBBBCCC'))
print(decodeString([('W', 5), ('A', 2)]))