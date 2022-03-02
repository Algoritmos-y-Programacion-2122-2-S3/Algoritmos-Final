def main():
    print("Welcome")
    word = input("Please give the word")
    position = len(word) - 1
    revert_word(word,position)

def revert_word(word,position):
    print(word[position],end="")
    if position == 0:
        return word[position]
    
    return revert_word(word,position-1)

main()