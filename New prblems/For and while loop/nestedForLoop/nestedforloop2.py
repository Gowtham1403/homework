######### Problem 1.1
#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67

#intialize the variable
studentCount = 0
markCount = 2
netMark1 = []
names = []

#get the input from user
studentCount = int(input("Enter the number of students: "))

#for loop for input and stores in list
for student in range (studentCount):
    names.append(input("Enter the name of the student : "))
    for mark in range (markCount):
        inputmark1 = int(input(f"Enter mark for student {names[student]} is : "))
        netMark1.append(inputmark1)
print(netMark1)

i = 0
marks = 0

#print the output addition of index value get the expected output

for student in range (studentCount):
    print(f"{names[i]}  marks are {netMark1[marks]} and {netMark1[marks+1]}")
    i += 1
    marks += 2
    
'''

Output :

Enter the number of students: 2
Enter the name of the student : gowtham
Enter mark for student gowtham is : 88
Enter mark for student gowtham is : 87
Enter the name of the student : sree
Enter mark for student sree is : 99
Enter mark for student sree is : 98
[88, 87, 99, 98]
gowtham  marks are 88 and 87
sree  marks are 99 and 98

'''