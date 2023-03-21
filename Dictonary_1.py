letter = ''
letterOccurance = {} 
while (letter.lower() != 'z'):
    letter = input("Enter a character: ")

    if letter in letterOccurance:
        letterOccurance[letter] += 1
    else:
        letterOccurance[letter] = 1

print(letterOccurance)