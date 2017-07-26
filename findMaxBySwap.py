__author__ = 'kathan'


def swapAdjacent(array, index):
    temp = array[index]
    array[index] = array[index - 1]
    array[index - 1] = temp


def swap(array, src_index, dest_index):
    for i in range(dest_index, src_index, -1):
        swapAdjacent(array, i)


def findMaxBySwap(array, k):
    max_swap = 0
    moving_index = 0

    while max_swap < k and moving_index < len(array):

        max_index = moving_index
        range_index = moving_index + (k - max_swap) + 1 if moving_index + (k - max_swap) + 1 < len(array) else len(array) - 1

        for i in range(moving_index, range_index):
            if array[max_index] < array[i]:
                max_index = i

        if max_index != moving_index:
            swap(array, max_swap, max_index)
            max_swap = max_index - moving_index + max_swap

        moving_index += 1

    return array

print findMaxBySwap([1, 5, 2, 9, 3], 3)
print findMaxBySwap([9, 8, 7, 6, 5], 3)
print findMaxBySwap([1, 5, 2, 9, 6], 4)