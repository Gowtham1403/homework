'''
1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.
'''

alphabetCount = 0
splCharCount = 0
NumberCount = 0
alphabets = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","i","I","K","k","L","l","m","M","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
splChar = ["!","@","#","$","%","^","&","*","<",">","?","/","_"]


password = input("Enter the password in minimum 8 digits :")
LenghtOfPassword = len(password)
if LenghtOfPassword >= 8:
    for i in password :
        if i in alphabets :
            alphabetCount = alphabetCount + 1
        if i in numbers :
            NumberCount = NumberCount + 1
        if i in splChar :
            splCharCount = splCharCount +1
    if alphabetCount >= 3 and NumberCount >= 2 and splCharCount >= 1 :
        if LenghtOfPassword >= 16:
            print("Your Password is Very Strong.....")
        else :
            print("Your  Password is Strong")
    elif alphabetCount == LenghtOfPassword or NumberCount == LenghtOfPassword or splCharCount == LenghtOfPassword :
        print("Your Password is Weak")
    elif alphabetCount >= 1 or NumberCount >= 1 or splCharCount >= 1 :
        if alphabetCount >= 1 and NumberCount >= 1 and splCharCount >= 1 :
            print("Your Password is Ok")
        else:
            print("Your Password is moderately Ok")

else:
    print("Your  Password must contain minimum 8 characters...So  Please enter Valid Password...")
