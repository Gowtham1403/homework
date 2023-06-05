######## Problem 1 ###############
#write multiplication table like this
# 1 * 1 = 1
# 1 * 2 = 2
#etc. Get the number as input

#get the input 
multiplicationNumber = int (input("Enter the multiplication number for print table: "))
NoOfRows = int (input("How many number of rows do you want to print: "))
#for loop for run the table
for i in range (1 , NoOfRows+1):
    result = i * multiplicationNumber
    print (i , "*" , multiplicationNumber , " = ", result)


'''
Output:

Enter the multiplication number for print table: 14
How many number of rows do you want to print: 10
1 * 14  =  14
2 * 14  =  28
3 * 14  =  42
4 * 14  =  56
5 * 14  =  70
6 * 14  =  84
7 * 14  =  98
8 * 14  =  112
9 * 14  =  126
10 * 14  =  140
'''