letter = ''
letterOccurance = {} #keyword is the char and value is the count of the char
while (letter.lower() != 'z'):
    letter = input("Enter a character: ")

    if letter in letterOccurance:
        letterOccurance[letter] += 1
    else:
        letterOccurance[letter] = 1

print(letterOccurance)