import random


class Mastermind:

    def __init__(self, length=6, attempt=10):
        self.__length = length  # code length
        self.__attempt = attempt  # maximum attempt
        self.__puzzle = []  # game solution
        self.__ans_list = []  # user attempt list
        self.__code = [1, 2, 3, 4, 5, 6]  # number of code

    def create_puzzle(self):
        for i in range(int(self.__length)):
            self.__puzzle.append(str(random.choice(self.__code)))

    def play(self):
        value = list(input("What is your guess?: "))
        while len(value) != self.__length:
            print(f"The code must be {self.__length} digit long, please try again")
            value = list(input("What is your guess?: "))
        timer = 0
        for i in range(self.__attempt):
            print(f"Your guess is {''.join(value)}")
            for i in range(len(self.__puzzle)):
                if value[i] == self.__puzzle[i]:
                    print("*",end="")
                elif value[i] in self.__puzzle:
                    print("o",end="")
                else:
                    print(".",end="")
            timer += 1
            self.__ans_list.append(value)
            print()
            if value == self.__puzzle:
                break
            if timer == self.__attempt:
                break
            value = list(input("What is your guess?: "))
            while len(value) != self.__length:
                print(f"The code must be {self.__length} digit long, please try again")
                value = list(input("What is your guess?: "))
        if timer == self.__attempt and value != self.__puzzle:
            print("You have failed to solve the puzzle")
            print()
        else:
            print(f"You solve it after {timer} rounds")
            print()

    def summarize(self):
        print("Game summarize")
        print(f"The answer is {''.join(self.__puzzle)}")
        for i in range(len(self.__ans_list)):
            print(f"Your #{i+1} guess is {''.join(self.__ans_list[i])}")


game = Mastermind(6, 10)
game.create_puzzle()
game.play()
game.summarize()

