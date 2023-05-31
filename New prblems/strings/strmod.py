########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("enter the string : ")
pigLatinKey = 'ay'
vowles = ['a','e','i','o','u']


for word in inputSentence.split(): #get the word in a sentence
    #take the first char
    firstVowel = 0
    firstLetter = word[0]
    if len(word)>1:#check if the word has more than one char
        for index,char in enumerate(word):
            if char.lower()in vowles:
                firstVowel = index + 1
                break
    word = word[firstVowel:] + word[:firstVowel] + pigLatinKey
    print(word , end=' ')
    
'''
Output:

enter the string : I am Python
Iay maay nPythoay 

'''