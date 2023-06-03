########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g


inputString = input("Enter a string: ")
i = 0  
newString = ""

while i < len(inputString):
    newString += inputString[i:i+2] #by slicing we add index 0 and 1
    newString += " "  # add space
    i += 2

print (newString)

'''
Output:

Enter a string: sayur
sa yu r 

'''