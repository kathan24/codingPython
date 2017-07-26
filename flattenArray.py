__author__ = 'kathan'

def flattenArrayIterative(array):
    i = len(array)
    result = []
    index = 0
    while i > 0:
        if isinstance(array[index], list):
            i += len(array[index]) - 1
            temp_index = index
            temp_array = array[index]
            del array[index]
            for j in range(len(temp_array)):
                array.insert(temp_index, temp_array[j])
                temp_index += temp_index
        else:
            result.append(array[index])
            i -= 1
            index += 1

    return result


def flattenArrayRecursively(array):
    length = len(array)
    res = []
    for i in range(length):
        if isinstance(array[i], list):
            res = res + flattenArrayRecursively(array[i])
        else:
            res.append(array[i])
    return res


if __name__ == '__main__':
    a = [1, [2, [3, [4, [5, [6]]]]]]
    print flattenArrayIterative(a)
    print flattenArrayRecursively(a)