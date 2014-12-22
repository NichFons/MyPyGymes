#####Hacking Game#####
#User gets 5 guesses #
#to guess the right  #
#word in a list with #
########hints#########

from random import sample
import TKinter as tk


screen = tk.Tk("Hacking Game")
# Takes the setting and creates a file ID and the correct number of words
# Returns a list of words
def grabWords(setting):
    words = ["./text_files/very_easy.txt", "./text_files/easy.txt", \
             "./text_files/medium.txt", "./text_files/hard.txt", \
             "./text_files/very_hard.txt"]
    number = [6, 7, 8, 9, 10]
    word_file = open(words[setting - 1])
    right_words = [i.strip('\n') for i in word_file]
    return sample(right_words, number[setting - 1])

# The actual game loop, that takes a guess and checks it!
# Returns if the game is won or not
def game_loop(correct_word, word_list, guess_num):
    guess = input("Guess #{}: ".format(guess_num))
    if (guess not in word_list):
        print("Word is not in the list")
        return False
    else:
        correct = 0
        for i in range(len(guess)):
            if (guess[i] == correct_word[i]):
                correct+= 1
        print("{} / {} correct.".format(correct, len(guess)))
        if (correct == len(guess)):
            return True
        
        else:
            return False

# Put it all together
def hack():
    diff = input("Enter difficulty(1-5): ")
    try:
        # If it isn' it
        diff = int(diff)
    except ValueError:
        # Make it not pass number check
        diff = 0
    if diff > 0 and diff < 6:
        words = grabWords(int(diff))
    else:
        print("Please input integer 1-5")
        hack()
        return
    password = sample(words, 1)[0] # Sample returns a list, get the only thing
    for i in words:
        print(i)
    print()
    for i in range(1,5):
        win = game_loop(password, words, i)
        if win:
            print("You win!")
            break
    play = input("Enter 0 to play again, else to quit: ")
    if play == '0':
        print('\n\n\n')
        hack()


hack()

            
            
