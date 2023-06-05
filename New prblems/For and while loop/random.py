####### Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

#import random for choose any number by computer
import random
RandomComputerNo = print(random.randint(3, 9))
#initialize attempts
attempt = 0
#while cond for infinite times
while(True):
    UserGuessNo = int (input("Enter any number between 03 to 09 : "))
    if UserGuessNo >= RandomComputerNo:
        print("The number u guess is high")
    else:
        print("The number u guess is low")
    if UserGuessNo == RandomComputerNo:
        print("User Guess and Computer Random Guess are equal")
        break
    attempt +=1
    print (f"User Guessed the correct number in {attempt} attempts")
    
'''
Output:

'''
