import string

def get_inputs():
    return input("Please give me a phrase to verify:\n")

def verify_phrase_pangrama(phrase,alphabet):
    new_alphabet = list(alphabet)
    for letter in phrase:
        if new_alphabet.count(letter.lower()) > 0:
            new_alphabet.remove(letter.lower())
    return new_alphabet

def verify_phrase_count_letters(phrase,alphabet):
    result = set()
    for letter in alphabet:
        if str(phrase).lower().count(letter) > 1:
            result.add(letter)
    print(result)
    return result

def print_results(result_pangrama, result_letters):
    if len(result_pangrama) == 0:
        print("\nThe phrase is a Pangrama")
    else:
        print("\nThe phrase is not a Pangrama")

    print(f'La cantidad de letras repetidas son: {len(result_letters)}')

def main():
    phrase = get_inputs()
    alphabet = set(string.ascii_lowercase)
    result_alphabet_pangrama = verify_phrase_pangrama(phrase = phrase, alphabet = alphabet)
    result_alphabet_letters = verify_phrase_count_letters(phrase = phrase, alphabet = alphabet)
    print_results(result_pangrama = result_alphabet_pangrama, result_letters = result_alphabet_letters)
    


main()