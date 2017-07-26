__author__ = 'kathan'

def findKthSmallestSum(m, n, k):
    if len(m) == 0 or len(n) == 0 or k <= 0:
        raise Exception("Invalid Argument")

    sum = m[0] + n[0]
    rank = 0
    i = 0
    j = 0

    while i < len(m) and j < len(n):
        if m[i] + n[j] >= sum:
            sum = m[i] + n[j]
            rank += 1

        if rank == k:
            break

        if i == len(m) - 1:
            j += 1
        elif j == len(n) - 1:
            i += 1
        elif m[i + 1] + n[j] > m[i] + n[j + 1]:
            if j > 0 and m[i + 1] + n[j - 1] < m[i] + n[j + 1]:
                i += 1
                j -= 1
            else:
                j += 1
        else:
            if i > 0 and m[i - 1] + n[j + 1] < m[i + 1] + n[j]:
                i -= 1
                j += 1
            else:
                i += 1

    if rank < k:
        raise Exception("There is no {0}th smallest sum")

    return sum

print findKthSmallestSum([1,2,3], [4,5,6], 5)
# (1, 4) (2, 4) (1, 5) (2, 5) (3, 5) (2, 6) (3, 6)
# 5 6 6 7 7 7 8 8 9