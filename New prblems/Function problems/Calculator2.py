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

#main code
MathsTotal = 0
MathsAvg = 0
ScienceTotal = 0
ScienceAvg = 0
HistoryTotal = 0
HistoryAvg = 0
NoOfSubjects = 3

 
marksInMaths = [56,78,56,45,90]
for MathsMark in marksInMaths:
    MathsTotal = addTwoNumbers (MathsTotal , MathsMark)
    MathsAvg = divideAFromB (MathsTotal , len(marksInMaths))
print(f'Your Total Mark in Maths is : {MathsTotal} and Your Avg of Maths Marks is : {MathsAvg}')


marksInScience = [90,78,67,8,98]
for ScienceMark in marksInScience:
    ScienceTotal = addTwoNumbers (ScienceTotal , ScienceMark)
    ScienceAvg = divideAFromB (ScienceTotal , len(marksInScience))
print(f'Your Total Mark in Science is : {ScienceTotal} and Your Avg of Science Marks is : {ScienceAvg}')


marksInHistory = [87,44,56,34,90]
for HistoryMark in  marksInHistory:
    HistoryTotal = addTwoNumbers (HistoryTotal , HistoryMark)
    HistoryAvg = divideAFromB (HistoryTotal , len(marksInHistory))
print(f'Your Total Mark in History is : {HistoryTotal} and Your Avg of History Marks is : {HistoryAvg}')

#Call divide function to get the average from all three subjects

AverageOfTwoSubject = addTwoNumbers(MathsAvg , ScienceAvg)
AverageOfAllSubjects = addTwoNumbers(HistoryAvg , AverageOfTwoSubject)
#Call divide function to get the average from all three subjects
#FillinMissingCode
avg = divideAFromB ( AverageOfAllSubjects , NoOfSubjects)
print(f"The total average of all three subjects : {AverageOfAllSubjects}")
print(f"The average mark is : {avg}")


'''
Output:

Your Total Mark in Maths is : 325 and Your Avg of Maths Marks is : 65.0
Your Total Mark in Science is : 341 and Your Avg of Science Marks is : 68.2
Your Total Mark in History is : 311 and Your Avg of History Marks is : 62.2
The total average of all three subjects : 195.39999999999998
The average mark is : 65.13333333333333
'''