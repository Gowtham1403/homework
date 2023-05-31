#empty box pattern

#get the length and width from user
length = int(input("Enter the length of the rectangle: "))
width =  int(input("Enter the width of the rectangle: "))

#for loop begins for column
for col in range(width):
    temp = ''
#for loop for row
    for row in range(length):
    #if cond is for chk row is 0 or last value similar to col
        if row == 0 or row == length - 1 or col == 0 or col == width - 1:
        #if if cond is true add '*' to variable
            temp += '*'
            continue
        #continue that add empty string
        temp += ' '
    print(temp)
        
'''      
Output:


Enter the length of the rectangle: 5
Enter the width of the rectangle: 6
*****
*   *
*   *
*   *
*   *
*****


'''