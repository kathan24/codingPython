__author__ = 'kathan'

"""
SOLUTION

bat
bear
cat
ear
ebb

iterate dictionary and check first letter.
if first letter of first word is same as first letter of next word then add remaing letters of those two words
    to a list and recurse
else create a relation in a way that key is the dependent and value is a list of all letter who are predesor
    like e -> [a,c] from word bat/bear and cat/ear

After relationship if formed, iterate all letters in dictionary which are not present in relationship. that will give
list of letters without any relationship

In order to create a word with relationship, find the letter in relationship VALUE (and not key) which either
does not have a key or does have a key with empty list
keep recursing until all list are empty
"""
def find_relationship(dictionary_list, current_list, relationship):
    first_word = dictionary_list[0]

    for i in range(1, len(dictionary_list)):
        if first_word[0] == dictionary_list[i][0]:
            current_list.append(first_word[1:len(first_word)])
            current_list.append(dictionary_list[i][1:len(dictionary_list[i])])
            find_relationship(current_list, [], relationship)
        else:
            current_list = []
            if relationship.has_key(dictionary_list[i][0]) and first_word[0] not in relationship[dictionary_list[i][0]]:
                relationship[dictionary_list[i][0]].append(first_word[0])
            else:
                relationship[dictionary_list[i][0]] = [first_word[0]]
            first_word = dictionary_list[i]


def get_remaining_letters(relationship, dictionary_list):
    unique_letters = set()
    remaining_letters = set()

    for key in relationship:
        unique_letters.add(key)
        for letter in relationship[key]:
            unique_letters.add(letter)

    for word in dictionary_list:
        for letter in word:
            if letter not in unique_letters:
                remaining_letters.add(letter)

    return list(remaining_letters)


def form_word(result, relationship):
    for key in relationship:
        for letter in relationship[key]:
            if not relationship.has_key(letter) or (relationship.has_key(letter) and len(relationship[letter]) == 0):
                if letter not in result:
                    result.append(letter)
                relationship[key].remove(letter)

                # If all precedent letters added then add key as well
                if len(relationship[key]) == 0:
                    result.append(key)

                form_word(result, relationship)

                break


relationship = {}
dictionary_list = ["bat", "bear", "cat", "ear", "ebb"]
find_relationship(dictionary_list, [], relationship)
print relationship

remaining_letters = get_remaining_letters(relationship, dictionary_list)

result = []
form_word(result, relationship)
result.extend(remaining_letters)

print "".join(result)