import random

correct = 'you guessed correctly!!!'
too_low = 'too low!!'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 10


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    low = int(input("Choose the lowest number you want to guess from:\n"))
    high = int(input("Choose the highest number you want to guess to:\n"))
	
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    while True:
        try:
            guess = int(input('Guess the secret number? '))       
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return guess 

			
def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    while True:

        (low, high) = configure_range()
        secret = generate_secret(low, high)
        guessCount = 0

        while True:
            guess = get_guess()
            guessCount += 1
            result = check_guess(guess, secret)
            print('You guessed ' + str(result) + ' in ' + str(guessCount) + ' guesses')

            if result == correct:
                break

        get_user_choice = input('Play again y or n')
        if get_user_choice.lower() == 'n':
            break


if __name__ == '__main__':
    main()
