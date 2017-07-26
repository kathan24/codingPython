__author__ = 'kathan'

def swap(array, start, dest):
    min_index = start
    for i in range(start, len(array)):
        if array[min_index] > array[i]:
            min_index = i

    temp = array[min_index]
    array[min_index] = array[dest]
    array[dest] = temp

    return array[0:start] + sorted(array[start:len(array)])

def findSmallestNumberGreaterThanGivenNumberWithSameDigits(array):
    for i in range(len(array) - 1, 0, -1):
        if array[i] > array[i - 1]:
            return ''.join(swap(array, i, i - 1))

    return 'Not possible'

number = '218765'
print findSmallestNumberGreaterThanGivenNumberWithSameDigits(list(number))

number = '1234'
print findSmallestNumberGreaterThanGivenNumberWithSameDigits(list(number))

number = '4321'
print findSmallestNumberGreaterThanGivenNumberWithSameDigits(list(number))

number = '534976'
print findSmallestNumberGreaterThanGivenNumberWithSameDigits(list(number))