__author__ = 'kathan'


def getWordFromString(str, startIndex):
    temp = ''
    while startIndex < len(str):
        if str[startIndex] == ' ':
            break
        temp += str[startIndex]
        startIndex += 1

    return temp

def wrapSentence(str, line_length):
    if len(str) < line_length:
        return str

    length_so_far = 0
    result = ''
    i = 0
    while i < len(str):
        word = getWordFromString(str, i)

        if len(word) <= line_length:
            if len(word) + length_so_far + 1 <= line_length:
                length_so_far += len(word) + 1
            else:
                result += '\n'
                length_so_far = len(word) + 1

            result += word + " "
            i += len(word) + 1
        else:
            raise Exception('Line length is smaller than the longest word "{}"'.format(word))

    print result


str = "A very long string containing many many words and characters. Newlines will be entered at spaces."
wrapSentence(str, 30)