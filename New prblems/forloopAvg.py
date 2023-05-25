#write code for both for and while loop
#Get marks from 5  students and calculate avg
#

#for loop
total = 0
for i in range(5):
    mark = int(input(f"Enter the mark of student{i+1} : "))
    total += mark
    avg = total / 5
print (f"Average mark is: {avg}")

'''
Output:
    
Enter the mark of student1 : 80
Enter the mark of student2 : 100
Enter the mark of student3 : 80
Enter the mark of student4 : 100
Enter the mark of student5 : 100
Average mark is: 92.0
'''