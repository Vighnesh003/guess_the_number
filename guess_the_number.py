import random

def guess_the_number():
    
    number_to_guess = random.randint(1, 100)

    
    attempts = 0

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        
        user_guess = int(input("Enter your guess: "))

        
        attempts += 1

        
        if user_guess == number_to_guess:
            print(f"Congratulations You guessed the number in {attempts} attempts!")
            break
        
        elif user_guess > number_to_guess:
            print("Your guess is too high. Try again!")
           
        else:
            print("Your guess is too low. Try again!")

if __name__ == "__main__":
    guess_the_number()