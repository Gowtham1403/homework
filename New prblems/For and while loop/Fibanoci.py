######## Problem 2 ###############
#Write a program that prints out the Fibonacci sequence up to a given number.
#example 1,2,3,5,8 , next number is the sum of previous two numbers.

#initialize and get the user
sum=0
MaximumLimit = int ( input ("Enter the maximum limit of the fibonacci series :"))
#for loop for run
for num in range ( 1, MaximumLimit + 1 ):
    sum += num #Add the number one by one to variable sum
    print(sum ,"," , end = " ") #print that sum


'''
Output:

Enter the maximum limit of the fibonacci series :10
1 , 3 , 6 , 10 , 15 , 21 , 28 , 36 , 45 , 55
'''