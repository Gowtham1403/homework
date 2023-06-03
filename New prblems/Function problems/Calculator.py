#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#The main function adds all student marks and finds the average

def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans
def subtractAfromB(a, b):
    ans = b - a
    return ans
def multiplyTwoNumbers(n1,n2):
    ans = n1 * n2
    return ans
def divideAFromB(numerator , denominator):
    ans = numerator / denominator
    return ans



#Get 5 marks from student and find the total
noOfSubjects = 5
total = 0
for i in range(noOfSubjects):
    mark = int(input(f" Enter the stuent mark : "))#correct te syntax as needed
    total=addTwoNumbers(total , mark)
print("TOTAL MARK : ",total)
#Call divide function to get the average
#FillinMissingCode
avg=divideAFromB(total,noOfSubjects)
print("The avg mark is ",avg)


'''
Output:
 Enter the stuent mark : 50
 Enter the stuent mark : 50
 Enter the stuent mark : 50
 Enter the stuent mark : 60
 Enter the stuent mark : 70
TOTAL MARK :  280
The avg mark is  56.0
'''

