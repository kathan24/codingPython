__author__ = 'kathan'


class Node():
    def __init__(self, prefix):
        self.prefix = prefix
        self.children = {}
        self.is_word = False

trie = Node("")

def insertWords(word):
    global trie

    current = trie
    for index, char in enumerate(word):
        if char not in current.children:
            current.children[char] = Node(word[0:index + 1])
        current = current.children[char]
    current.is_word = True


def autoComplete(dictionary):
    for word in dictionary:
        insertWords(word)


def findAllWords(node, results):
    if node.is_word:
        results.append(node.prefix)

    for char in node.children:
        findAllWords(node.children[char], results)


def getWordsForPrefix(prefix):
    results = []
    global trie
    current = trie

    for char in prefix:
        if char in current.children:
            current = current.children[char]
        else:
            return results

    findAllWords(current, results)
    return results

autoComplete(["abc", "acd", "bcd", "def", "a", "aba"])
print getWordsForPrefix('ab')
print getWordsForPrefix('b')