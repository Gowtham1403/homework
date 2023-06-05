########### Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

       
inputSentence = input("Enter the input as sentence : ")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u']
for word in inputSentence.split():
    #take the first char
    FirstIndexVowel = 0
    firstChar = word[0] #start from 0
    if len(word)>1: #check if the word has more than one char
        for index,char in enumerate(word):
            if char.lower() in vowels:
                FirstIndexVowel = index + 1

    word = word [FirstIndexVowel:] + word [:FirstIndexVowel] + pigLatinKey
    print(word , end=' ')

'''
Output:

Enter the input as sentence : I am python
Iay maay npythoay 
'''