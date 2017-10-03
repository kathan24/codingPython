__author__ = 'kathan'


def fullJustify(words, maxWidth):
    output_list = []
    word_ptr = 0

    while word_ptr < len(words):
        len_so_far = 0
        words_so_far = []

        while len_so_far < maxWidth and word_ptr < len(words):
            temp_length = len_so_far + len(words[word_ptr])
            if temp_length > maxWidth:
                break
            words_so_far.append(words[word_ptr])
            len_so_far = len_so_far + len(words[word_ptr]) + 1
            word_ptr += 1

        spaces_array = []
        if len(words_so_far) > 1:
            len_diff = maxWidth - (len_so_far - len(words_so_far))
            num_of_space_after_each_word = len_diff / (len(words_so_far) - 1)
            remaining_spaces = len_diff % (len(words_so_far) - 1)

            spaces_array = [num_of_space_after_each_word] * (len(words_so_far) - 1)

            if remaining_spaces != 0:
                for i in range(remaining_spaces):
                    spaces_array[i] += 1

        line_formation = ""
        for index, word in enumerate(words_so_far):
            if index < len(spaces_array):
                line_formation += word + (' ' * spaces_array[index])
            else:
                line_formation += word + (' ' * (maxWidth - len(line_formation + word)))

        output_list.append(line_formation)
        if line_formation == "":
            break

    return output_list

print fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print fullJustify(["What", "must", "be", "shall", "be."], 12)
print fullJustify([""], 0)