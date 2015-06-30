# Number -> Number
# asks the user for a number, guesses the number and asks
# if the guess is too high, too low, or correct
low = 0
high = 100
response = ''

print("Please think of a number between 0 and 100!")

while (True):
    ans = (high + low) / 2
    
    print("Is your secret number " + str(ans) +"?")
    response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if response == 'h':
        high = ans    
    elif response == 'l':
        low = ans    
    elif response == 'c':
        return("Game over. Your secret number was: " + str(ans))
    else:
        print("please enter either 'h', 'l', or 'c'")
        
