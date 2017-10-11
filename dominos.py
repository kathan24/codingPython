__author__ = 'kathan'


class Domino(object):
    MAX_DOT = 3

    def __init__(self, first_half, second_half):
        self.first_half = first_half
        self.second_half = second_half


class DominoBag(object):
    def __init__(self):
        self.domino_list = []

    def add(self, domino):
        self.domino_list.append(domino)

    # There should be dominos like [0 | 1] [1 | 2] [2 | 3] ...... [MAX_DOT - 1 | MAX_DOT]
    def all_unique(self):
        unique_domino_list = [False for i in range(Domino.MAX_DOT)]

        for domino in self.domino_list:
            if domino.first_half + 1 == domino.second_half or domino.second_half + 1 == domino.first_half:
                unique_domino_list[min(domino.first_half, domino.second_half)] = True

        return all(unique_domino_list)

    # check if there is a loop in domino like [0 | 1] [1 | 2] [2 | 0]
    def is_loop(self, base, current_list, parent=None):
        if base in current_list:
            return True

        for domino in self.domino_list:
            if domino == parent:
                continue

            if domino.first_half == base or domino.second_half == base:
                other = domino.first_half if domino.second_half == base else domino.second_half
                current_list.append(base)
                result = self.is_loop(other, current_list, domino)
                if result:
                    return result

        return False

domino1 = Domino(0,1)
domino2 = Domino(2,3)
domino3 = Domino(1,2)
domino_bag = DominoBag()
domino_bag.add(domino1)
domino_bag.add(domino2)
domino_bag.add(domino3)

print domino_bag.all_unique()

domino4 = Domino(0,1)
domino5 = Domino(1,2)
domino6 = Domino(2,0)
domino_bag1 = DominoBag()
domino_bag1.add(domino4)
domino_bag1.add(domino5)
domino_bag1.add(domino6)
print domino_bag1.is_loop(0, [])
