'''
Write an app for a phone sales man. The Salesman earns Rs10000 every month.
He earns Rs1000 commission for every phone he sells. If he sells more than 5 phones a month,
he earns extra Rs100 per phone (1000+100). If he sells 10 phones or more, 
he gets extra Rs 200 for each phone over 10. He can only earn max 25000 per month. 
He gets a bonus of Rs 25000 per year if he sells more than 100 phones in a year. 
Calculate his monthly salary and avg salary per month in one year. 
'''


earningEveryMonth = 10000
commissionForPhone = 1000
bonusFor5phones = 100
bonusFor10phones = 200
salary = 0 
yearlySalary = 0 
yearlySales = 0
AvgMonthlySalary = 0
bonusFor100phones = 25000
maxEarnings = 25000
Totalmonths = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthlySalary = []
for i in range (len(Totalmonths)):
    sales = int(input(f"Enter  your {Totalmonths[i]} Sales: "))
    if  sales <= 4:
        salary = (sales * commissionForPhone)
    elif sales >= 5:
        salary = (sales * commissionForPhone + bonusFor5phones)
    elif sales >= 10 :
        sales = sales - 10
        salary = (sales * commissionForPhone + bonusFor5phones)
    salary = salary + earningEveryMonth
    if salary > 25000:
        salary = maxEarnings
    monthlySalary.append(salary)
    yearlySalary = yearlySalary + salary
    yearlySales = yearlySales + sales
for i in range (len(Totalmonths)):
    print(f"Your {Totalmonths[i]} salary is {monthlySalary[i]}")
if yearlySales >= 100:
    yearlySalary = yearlySalary + bonusFor100phones
AvgMonthlySalary = yearlySalary / 12
print(f"Your yearly Salary is : {yearlySalary}")
print(f"Your Average yearly salary is : {AvgMonthlySalary}")