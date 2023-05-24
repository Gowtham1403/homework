'''
Check if the username and password is correct. 
Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
name of the company mentioned in the username, followed by any 3 numbers.
eg username : myname@sayur.com. password - mnamesay123 
'''
num = ["0","1","2","3","4","5","6","7","8","9"]
username = input("Enter the Username : ")
if ("@" in username ) and (".edu" in username or ".com" in username or ".tech" in username or ".org" in username):
    password = input ("Enter your password : ")
    index = username.index("@")
    CorrectPassword = ""
    CorrectPassword = username [0] + username [2] + username [index - 3] + username [index - 2] + username [index - 1] + username [index + 1] + username [index + 2] + username [index + 3]
    CorrectPassword = CorrectPassword + password [-3] + password [-2] + password [-1]
    if password [-3] in num and password [-2] in num and password [-1] in num : 
        if CorrectPassword == password :
            print("Your Username is verified")
            print(f"Hai {username} !!")
    else:
        print("Please enter the valid password")
else:
    print("please enter the valid username")