import random, time

secretNumber = random.randint( 1, 20 )
name = input('What is your name? ')
print("Well " + name + ", guess the secret number")

for guesses in range (1,5):
    guess = int(input( 'Take a guess '))
    if guess == secretNumber:
        print( "correct, the number is " + str(secretNumber))
        time.sleep(3)
    elif guess > secretNumber:
            print( 'Too high ')
    elif guess < secretNumber:
            print( 'Too low ')
    else:
        break
print('You took ' + str(guesses) + ' guesses.') 
