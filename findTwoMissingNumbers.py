__author__ = 'kathan'


def find_two_nums(arr):

    # XOR of all the numbers from 1 .... n
    xor_all = 1
    for i in range(2, len(arr) + 2 + 1):
        xor_all ^= i

    # XOR of all numbers in array
    xor_array = arr[0]
    for i in range(1, len(arr)):
        xor_array ^= arr[i]

    diff_value = xor_array & xor_all

    # find rightmost set bit
    right_most_set_index = 0

    binary_list = list(bin(diff_value))[2:]
    for i in range(len(binary_list) - 1, -1, -1):
        if int(binary_list[i]):
            right_most_set_index = i
            break

    # number with that index
    number = 1 << right_most_set_index

    print "One missing number: " + str(xor_all ^ number)
    print "Second missing number: " + str(xor_array ^ number)


find_two_nums([1, 2, 3, 4, 6, 7, 8, 10])
