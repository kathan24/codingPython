__author__ = 'kathan'

def printCombinations(items, target, current_list):
    if target == 0:
        print current_list
    elif target < 0:
        return

    for i in range(len(items)):
        current_list.append(items[i])
        printCombinations(items, target - items[i], current_list)
        del current_list[-1]


printCombinations([3,9,8,4,5,7,10], 10, [])
