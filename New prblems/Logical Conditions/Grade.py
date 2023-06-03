############## Problem 4 ##############
#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

mark1 = int(input("Enter the first mark:"))
mark2 = int(input("Enter the second mark: "))
mark3 = int(input("Enter the third mark: "))
if(mark1 == 100 or mark2 == 100 or mark3 == 100):#at least one mark is 100
    print ("Your Grade is A")
elif(mark1>=90 or mark2>=90 or mark3>=90):# atleast one 90
    print ("Your Grade is B")
elif(mark1>=60 or mark2>=60 or mark3>=60):
    print("Your Grade is C")
elif(mark1<=50 and mark2<=50 and mark3<=50):
    print("Your Grade is F" )
else: 
    print ("Your Grade is D")


'''
Output:

Enter the first mark:40
Enter the second mark: 100
Enter the third mark: 50
Your Grade is A
'''