######## Problem   ###############
# Get and print the 2 marks for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

#intialize the variable
studentCount = 0
markCount = 2
netMark = []
names = []

studentCount = int(input("Enter the number of students : "))

#get the input from user
for student in range (studentCount):
    names.append(input("enter the name of the student: "))
    for mark in range (markCount):
        inputMark = (input(f"enter mark {mark+1} is : "))   
        netMark.append(inputMark)
print(netMark)

i=0
marksIndex=0

#print the output
for student in range (studentCount):
    for mark in range (markCount):
        print (f"Mark {mark+1} for {names[i]} is : {netMark[marksIndex]}")
        marksIndex+=1
    i+=1
    
'''
Output:

Enter the number of students : 2
enter the name of the student: gowtham
enter mark 1 is : 28
enter mark 2 is : 50
enter the name of the student: gow
enter mark 1 is : 70
enter mark 2 is : 90
['28', '50', '70', '90']  
Mark 1 for gowtham is : 28
Mark 2 for gowtham is : 50
Mark 1 for gow is : 70
Mark 2 for gow is : 90
'''