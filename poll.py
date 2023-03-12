'''
Take an opinion poll among students. Ask the students whether they like online class
(input as 1), in person class (input as 2) or mixed (input as 3).
Display the percentage of the female students that like online classes.
You can end the poll when someone answers 'No comment' (input as 4) or when the poll 
reaches at least 10 students.
'''
#PROGRAM :


female = 0
female_like_online_classes = 0
x = 0

while x < 10 :
    

    print(f"Number of polls left = {10-x}")


    Gender = input("Enter your sex (Male/Female) : ")


    print("1-Like online classes\n2-Like offline classes\n3-Like both online and offline classes\n4-NO")
    option = int(input("Enter ur option : "))


    if option > 4 or option < 1 :
        print("Enter a valid option") 
        continue


    x += 1


    if Gender.upper() == 'FEMALE' :
        female += 1


    if option == 4 :
        break


    elif Gender.upper() == 'FEMALE' and option == 1 :
        female_like_online_classes += 1


print(f"total number of polls = {x}")


print(f"number of Females voted = {female}")


if female != 0 :
    print(f"Female love online classes is { ( female_like_online_classes / female ) * 100 } % ")
    

print("END")