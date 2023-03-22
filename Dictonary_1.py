letter = ''
letterOccurance = {} 
while (letter.lower() != 'z'): # if the input is not equal to zero it is enter
    letter = input("Enter a character: ")

    if letter in letterOccurance:
        letterOccurance[letter] += 1
    else:
        letterOccurance[letter] = 1

print(letterOccurance)