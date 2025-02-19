import random
name = input (" What is your name?")
print("GoodLuck", name)

random_names = [ 'Pinapple' , 'Shampoo' , 'Basketball' , 'Notebook' , 'Python']
word = random.choice(random_names) # Picks randomly from random_names

print ("Guess a random ")

guesses = ' ' #starting with an empty string
turns = 10

while turns > 0:
    failed = 0

    for z in word:  #checking each letter in the word

        if z in guesses:
            print (z, end = '')  #if the word guesses is in word, print z, end = '' prints in the same line instead of the different line
        
        else:
            print('__') # prints nothing, expect for --
            failed += 1 # increases fail count to keep track

    if failed == 0: #if the fail count is 0
        print('Winner')
        print('The word is :' , word)
        break  #break from the game 
    print( )
    guess = input ("Guess a letter:") 
    guess += guess

    if guess not in word:   #if guessed letter is not in word
        turns -= 1   # deducts turn
        print('Wrong, boooo')
        print(' You have', + turns, 'more to guess')

        if turns == 0:
            print('You Loose, Looser')
