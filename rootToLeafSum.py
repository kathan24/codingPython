__author__ = 'kathan'


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_sum(node, total, current_list):
    if total < 0:
        return False

    total = total - node.value
    current_list.append(node.value)

    if not node.left and not node.right and total == 0:
        return True

    if node.left and find_sum(node.left, total, current_list):
        return True

    if node.right and find_sum(node.right, total, current_list):
        return True

    current_list.pop()
    return False


root = Node(15)
root.left = Node(10)
root.right = Node(20)

root.left.left = Node(6)
root.left.right = Node(7)

root.left.right.left = Node(2)
root.left.right.right = Node(16)

root.left.right.left.left = Node(1)
root.left.right.left.right = Node(5)

root.left.right.right.left = Node(3)

root.right.left = Node(22)


#                    15
#             10            20
#         6        7      22
#               2    16
#             1  5  3

lst = []
print find_sum(root, 35, lst)
print lst


