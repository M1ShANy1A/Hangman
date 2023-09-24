import random


class Hangman:
    __WORDS = ['galaxy', 'zodiac', 'zombie', 'wizard', 'wave', 'vape', 'generation']
    __WORD = random.choice(__WORDS)
    __MISTAKES = 0

    def __init__(self):
        word = list(self.__WORD)
        letter = random.choice(self.__WORD)
        for let in word:
            if let != letter:
                word[word.index(let)] = '_'
        self.word = ' '.join(word)
        print(self.word)

    def __bool__(self):
        if self.word.count('_') == 0 or self.__MISTAKES == 9:
            print("You lost.")
            return False
        return True

    def set_letter(self, letter):
        word = self.word.split(' ')
        word[self.__WORD.index(letter)] = letter
        return ' '.join(word)

    @staticmethod
    def is_valid(letter):
        if letter.isalpha():
            return True
        print("Your input must be a string.")
        return False

    def change_info(self):
        self.__MISTAKES += 1
        if self.__MISTAKES != 9:
            self.guess_letter()

    def guess_letter(self):
        letter = input("Guess a Letter: ")
        if self.is_valid(letter):
            if letter in self.__WORD:
                self.word = self.set_letter(letter)
                print(self.word)
                if '_' in self.word:
                    self.guess_letter()
            else:
                print(self.word)
                self.change_info()

    def play(self):
        while self:
            self.guess_letter()


if __name__ == '__main__':
    h = Hangman()
    h.play()