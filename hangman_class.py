import random
import time

def grab_words():

    wordlist = []

    with open("words.txt", "r") as words:
        for line in words:
            wordlist.append(line)

    return wordlist

class Words:

    def __init__(self, wordlist):
        self.word = wordlist[random.randint(0, len(wordlist) - 1)]

    def return_word(self):
        return self.word         

    def convert_word(self):
        return [char for char in self.word.strip("\n")]

class GameFunctions:

    def __init__(self, list_of_chars, word):
        self.list_of_chars = list_of_chars
        self.word = word
        self.list_of_underscores = []

    def take_input(self):
        user_input = str(input("Please input a letter:"))
        return user_input

    def return_lines(self):
        
        for a in self.list_of_chars:
            self.list_of_underscores.append("_")
        
        return self.list_of_underscores

    def display_lines(self):
        
        self.linestring = ' '.join(self.list_of_underscores)

        print(self.linestring)

    def hangman_art(self):
        
        HANGMANPICS = ['''
                        +---+
                        |   |
                            |
                            |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                            |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                        |   |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                       /|   |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                       /|\  |
                            |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                       /|\  |
                       /    |
                            |
                        =========''', '''
                        +---+
                        |   |
                        O   |
                       /|\  |
                       / \  |
                            |
                        =========''']

        return HANGMANPICS