#using while loop
total = 0
noOfStudents = 5
i = 0
while (i < noOfStudents):
    mark = int(input(f"Enter the mark of student{i+1} : "))
    total += mark
    i+=1
    avg = total / 5
print (f" Your Average mark is : {avg}")