'''
Write the function mostFrequentLetters(s), that takes a string s, and ignoring case 
(so "A" and "a" are treated the same), returns a lowercase string containing the letters of s in most 
frequently used order. (In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
'''

#PROGRAM :

s = "We Attack at Dawn"

s = s.lower()
s = s.replace(' ','')

UniqueLetter= sorted(set(s))

LetterCount = [0] * len(UniqueLetter)

for i , letter in enumerate(UniqueLetter) :

    LetterCount[i] = s.count(letter)

letterCountsTuples = list(zip(UniqueLetter, LetterCount))

sortedLetterCounts = sorted(letterCountsTuples, key=lambda x: (-x[1], x[0]))

result = ''.join([x[0] for x in sortedLetterCounts])

print(result)