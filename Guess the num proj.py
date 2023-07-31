import random 
EASY_LEVEL_ATTEMPTS =10
HARD_LEVEL_ATTEMPTS =5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number,answer,attempts):   
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"You are correct...The answer was indeed {answer}")  

def game():
    print("Hello, am Jarvis. Lets play a game where i will assign a number between 1 to 50 and you try guessing it!")
    answer=random.randint(1,50)
    level=input("Please choose the level of difficulty....Type in 'easy' or 'hard' :")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} remaining to guess the number")
        guessed_number=int(input("Guess a number :"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses.....lol,you lose!")
            return
        elif guessed_number!=answer:
            print("guess again")


game()
