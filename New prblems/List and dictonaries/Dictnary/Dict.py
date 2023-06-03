########## Program 1
#find the list unique words in a sentence
#hint - Each word is a key, count is the value

# Declare empty dictnoary
Dictwords={}
#declare a list
uniqueWords=[]
#user input
sentence = "This is a cat and it has a tail and two eyes"
#we split the sentence into words
SplitedLisit = sentence.split()
#for loop begins 
for word in SplitedLisit:
#here we check that word is not in the dict
    if word not in Dictwords:
        #insert in dict by Key = Value
        Dictwords[word] = 0
    #append the word in list
        uniqueWords.append(word)
    #if the word is in list we add the occurence value only
    Dictwords[word] += 1
print("Unique words in the sentence are : ")
#finaaly print the unique word 
print(f'{uniqueWords}')

'''
Output:
Unique words in the sentence are : 
['This', 'is', 'a', 'cat', 'and', 'it', 'has', 'tail', 'two', 'eyes']
'''