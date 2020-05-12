import hangman_class as hc

def main_loop():

    picked_word = hc.Words(hc.grab_words())
    word = picked_word.return_word()
    print(word)
    charlist = picked_word.convert_word()

    hangman = hc.GameFunctions(charlist, word)

    hangman.return_lines()
    hangart = hangman.hangman_art()

    error_count = 0

    playgame = True
    
    while playgame:

        hangman.display_lines()

        user_input = hangman.take_input()

        check_letter = True

        while check_letter:
            if user_input in hangman.list_of_chars:
                letter_index = [i for i, n in enumerate(hangman.list_of_chars) if n == user_input]
                for index in letter_index:
                    hangman.list_of_underscores[index] = user_input
                check_letter = False
            else:
                print("Try again!")
                error_count += 1
                print(hangart[error_count - 1])
                check_letter = False

        if error_count == len(hangart):
            print("Game over!")
            playgame = False
        else:
            continue

if __name__ == "__main__":
    main_loop()