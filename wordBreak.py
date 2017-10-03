__author__ = 'kathan'

def wordBreak(str, word_dict):
    if str in word_dict:
        return str

    for i in range(1, len(str)):
        pre_str = str[0:i]
        if pre_str in word_dict:
            remaining_str = str[i:len(str)]
            str_found = wordBreak(remaining_str, word_dict)
            if str_found:
                return pre_str + " " + str_found

word_dict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]

print wordBreak("ilike", word_dict)
print wordBreak("ilikesamsung", word_dict)
print wordBreak("mange", word_dict)
