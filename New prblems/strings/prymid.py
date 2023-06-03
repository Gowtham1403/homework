
#get the input
InputString = input("Enter your string : ")
#store the length in variable
length = len(InputString)
#for loop for how many word given by user and we allot equal no of rows in length
for row in range (length):
 #for loop for addition of row + 1 in each and every column   
    for col in range (row + 1):
#print the sting by using the col index and finish the line with empty space otherwise the print fn move to next line 
        print(InputString[col], end = '' )
#print new line for new row
    print()
    
    
'''
Output :
Enter your string : sayur
s
sa
say
sayu
sayur

'''