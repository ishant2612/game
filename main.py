import time
import random

print("Hello! Welcome to hangman.")
name = input("Enter your name: ")
print(f"Hello {name} , get ready to play hangman")
time.sleep(2)
print("You have to guess a word from (apple, border, circle, joke, happy, laugh, house, sleep, market)\n"
      "You will get 5 chances to guess it correct")
time.sleep(3)
print("The game is about to start\n"
      "All the best!!!!")
time.sleep(3)


def func():
    global chances
    global computer
    global count
    global play_game
    word_to_guess = ["apple", "border", "circle", "joke", "happy", "laugh", "house", "sleep", "market"]
    chances = 5
    count = 0
    computer = random.choice(word_to_guess)
    play_game = ""


def hint():
    global computer
    if computer == "apple":
        print("Hint:\n"
              "Should not fall on his head!! ")
    elif computer == "border":
        print("Hint:\n"
              "Should not exist!")
    elif computer == "circle":
        print("Hint:\n"
              "never went to its corner!!")
    elif computer == "joke":
        print("Hint:\n"
              "a random line that raise out dopamine\n"
              "(dopamine is a chemical that make us feel happy)")
    elif computer == "happy":
        print("Hint:\n"
              "Always be ______!!")
    elif computer == "laugh":
        print("Hint:\n"
              "Ha Ha Ha Ha!!!!")
    elif computer == "house":
        print("Hint:\n"
              "safest place!!")
    elif computer == "sleep":
        print("Hint:\n"
              "Should be of 8 hours")
    elif computer == "market":
        print("Hint:\n"
              "all money goes to _______!!")


def main():
    global count
    func()
    hint()
    while chances > count:
        guess = input("Enter your guess: ")
        count += 1
        if guess == computer:
            print("Congratulation! you win!!!!")
            play_loop()
        elif count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |       \n"
                  "  |       \n"
                  "  |       \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     o \n"
                  "  |   / | \ \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     |  \n"
                  "  |     O \n"
                  "  |   / | \ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. " + str(chances - count) + " guesses remaining\n")
            print(f"The correct word was {computer}!!")
            play_loop()


def play_loop():
    global play_game
    play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()


main()