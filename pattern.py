'''
Encoding problem - Input is a message and a pattern. Both stringd. Output is the message writtenin the form of the pattern.
Eg -    Message - "I Love India".
        Pattern - "*** **** ** **********      *****"
        Output - "ILo veIn di aILoveIndi      aILov"
    Note how you replace each * in the pattern with the letter in the message, the space in the message doesnt matter, but the space(s) in the patterns matters.
'''


pattern = '*** **** ** **********      *****'

message = input("Enter any quotes: ")
withoutSpaces = ""  


for word in message:    
    if word != " ": 
        withoutSpaces = withoutSpaces + word    

result = ''     


letters = []    
n = 0
for x in withoutSpaces:    
    letters.append(x)       
        

for i in pattern:   
 
    if i != ' ':     
        if n > (len(withoutSpaces) - 1):
            n= 0

            result = result + letters[n]
            n = n + 1   
        else:
           
            result = result + letters[n]
            n = n + 1   
    else: 
        result = result + i
             
print(result)