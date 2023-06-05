######### Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

inputSentence = input("Enter the input as sentence : ")
pigLatinKey = 'ay'
for word in inputSentence.split(): 
 
    firstChar = word[0]
    if len(word) >= 1 :
        word = word[1:] + firstChar + pigLatinKey
        print(word , end = ' ')

'''
Output:

Enter the input as sentence : I am python
Iay maay ythonpay 

'''