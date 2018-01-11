__author__ = 'kathan'

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minSum(node, sum):
    if node is None:
        return sum

    left_sum = minSum(node.left, node.value + sum)
    right_sum = minSum(node.right, node.value + sum)

    if left_sum < right_sum:
        return left_sum
    else:
        return right_sum


def maxSum(node, sum):
    if node is None:
        return sum

    left_sum = maxSum(node.left, node.value + sum)
    right_sum = maxSum(node.right, node.value + sum)

    if left_sum < right_sum:
        return right_sum
    else:
        return left_sum


root = Node(15)
root.left = Node(10)
root.right = Node(20)

root.left.left = Node(6)
root.left.right = Node(7)

root.left.right.left = Node(2)
root.left.right.right = Node(16)

root.left.right.left.left = Node(0)
root.left.right.left.right = Node(5)

root.left.right.right.left = Node(3)

root.right.left = Node(22)


print "Min: " + str(minSum(root, 0))
print "Max: " + str(maxSum(root, 0))