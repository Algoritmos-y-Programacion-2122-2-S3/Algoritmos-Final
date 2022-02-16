from unittest import result


def get_common_prefix(word_list):
    result = ""
    letter_position = 0
    for letter in word_list[0]:
        is_common = True
        for index_words in range(1,len(word_list)):
            word = word_list[index_words]
            if letter_position < len(word):
                if word[letter_position] != letter:
                    is_common = False
            else:
                is_common = False
        if is_common:
            result += letter
        letter_position += 1
    return result
            

def main():
    strs = ["flower","flow","flight"]
    print(get_common_prefix(strs))


main()