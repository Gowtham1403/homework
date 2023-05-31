############# Problem 1 ###########
#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.
'''
0 - 2.5 lakhs                  exempt
2.5 - 5 lakhs                  5%
5 - 7.5 lakhs                  10%
7.5 - 10 lakhs                 15%
10 - 12.5 lakhs                20%
12.5 - 15 lakhs                25%
above 15 lakhs                 30%
'''

salary = int (input("Enter the salary in numbers : "))

if salary >= 0 and salary <= 250000:
    print(f"There is no tax.....You are exemption..Your salary is {salary}")
elif salary >= 250001 and salary <= 500000:
    salary = salary * 0.05
    print(f'Your salary is deducted and your salary is {salary}')
elif salary >= 500001 and salary <= 750000:
    salary = salary * 0.10
    print(f'Your salary is deducted and your salary is {salary}')
elif salary >= 750001 and salary <= 1000000:
    salary = salary * 0.15
    print(f'Your salary is deducted and your salary is {salary}')
elif salary >= 1000001 and salary <= 1250000:
    salary = salary * 0.20
    print(f'Your salary is deducted and your salary is {salary}')
elif salary >= 1250001 and salary <= 1500000:
    salary = salary * 0.25
    print(f'Your salary is deducted and your salary is {salary}')
elif salary >= 1500001:
    salary = salary * 0.30
    print(f'Your salary is deducted and your salary is {salary}')
    
    
'''

Enter the salary in numbers : 15000
There is no tax.....You are exemption..Your salary is 15000

Enter the salary in numbers : 250001
Your salary is deducted and your salary is 12500.05

Enter the salary in numbers : 500006
Your salary is deducted and your salary is 50000.6

Enter the salary in numbers : 750007
Your salary is deducted and your salary is 112501.05

Enter the salary in numbers : 1000006
Your salary is deducted and your salary is 200001.2

Enter the salary in numbers : 1250005
Your salary is deducted and your salary is 312501.25

Enter the salary in numbers : 2000000
Your salary is deducted and your salary is 600000.0

'''