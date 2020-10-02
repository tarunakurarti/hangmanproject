from words import word_list
import random

def getRandom():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_'*len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries=6

    print('......HANGMAN GAME!......')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input('Enter your guess :').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('you have already guessed',guess)
            elif guess not in word:
                print(guess,"is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("GOOD JOB,",guess,"is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you  already guessed the word", guess)
            elif guess != word:
                print(guess,"is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess")
            print('.....GAME OVER.....') 
        print(display_hangman(tries))
        print(word_completion)
        if guessed:
            print("congrats,you guessed the word! you won! ")
        else:
            print("sorry, you ran out of tries. the word was not expected correct")

def display_hangman(tries):
    stages = [ #6 final stage: head, torso, both arms, both legs
            """
                 ------------
                    |     |
                    |     o
                    |    \\//
                    |     |
                    |    / \\
                    -
            """,
            #5 head, torso,both arms, and one leg
            """
                 ----------
                    |      |
                    |      o
                    |      |
                    |      /
                    -
            """,
            #4 head, torso, and both arms
            """
                 -------
                    |     |
                    |     o
                    |    \\//
                    |      |
                    |
                    -
            """,
            #3 head, torso, and one arm
            """   
                 --------
                    |      |
                    |      o
                    |     \\|
                    |      |
                    |
                    -
            """,
            #2 head and torso
            """
                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                    -
            """,
            #1 head
            """
                    --------
                    |      |
                    |      o
                    |      
                    |      
                    |
                    -
            """,
            #0 intial empty stage
            """
                    --------
                    |      |
                    |      
                    |      
                    |      
                     
                    -
            """,
        ]
    return stages[tries]



       
def main():
    word = getRandom()
    print(word)
    play(word)

    while input('do you want to play again(Y/N):').upper() == 'Y':
        word = getRandom()
        play(word)
main()


