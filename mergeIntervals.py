__author__ = 'kathan'

def mergeIntervals(array):
    array = sorted(array)
    result = [array[0]]

    for i in range(1,len(array)):
        previous = result.pop()
        if previous[1] >= array[i][0]:
            if previous[1] < array[i][1]:
                previous[1] = array[i][1]
            result.append(previous)
        else:
            result.append(previous)
            result.append(array[i])

    return result

print mergeIntervals([[1,3], [2,4], [5,7], [6,8]])
print mergeIntervals([[6,8], [1,9], [2,4], [4,7]])
