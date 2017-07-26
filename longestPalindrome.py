__author__ = 'kathan'

def isPalindrome(array, start, end):
    if start < 0:
        return False
    while start < end:
        if array[start] != array[end]:
            return False
        start += 1
        end -= 1
    return True


def longestPalindrome(array):
    result = ""
    for i in range(len(array)):
        result_length = len(result)
        if isPalindrome(array, i - result_length, i):
            result = array[i - result_length: i + 1]
        elif isPalindrome(array, i - result_length - 1, i):
            result = array[i - result_length - 1: i + 1]

    print result


longestPalindrome('bbabb')
longestPalindrome('bbaaybcb')