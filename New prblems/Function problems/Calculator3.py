#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#add new functions as needed.

#The main functions is to find the total profit

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


#we have sales data for a week. 
costOfCoffee, costOfTea, costOfVadai = 25,20,25

coffeeSales = [56,78,56,45,90, 103,120]
teaSales = [100,123,456,123,222,400,346]
vadaiSales = [23,45,67,12,89,90,120]
TotalCoffeeSales = 0
TotalTeaSales = 0
TotalVadaiSales = 0
NoOfDaysPerWeek = 7
NoOfWeekPerMonth = 4
NoOfItems = 3

#Find total sales in the week.
#calculate avg sales for a week
for coffee in coffeeSales:
    TotalCoffeeSales = addTwoNumbers ( TotalCoffeeSales , coffee )
print(f"Total sales of coffee in a week is : {TotalCoffeeSales}")

for tea in teaSales:
    TotalTeaSales = addTwoNumbers ( TotalTeaSales , tea )
print(f'Total sales of tea in a week is : {TotalTeaSales}')

for vadai in vadaiSales:
    TotalVadaiSales = addTwoNumbers ( TotalVadaiSales , vadai )
print(f'Total sales of vadai in a week is : {TotalVadaiSales}')

TotalSalesOf2Items = addTwoNumbers ( TotalTeaSales , TotalCoffeeSales )
TotalSalesOfWeek = addTwoNumbers ( TotalSalesOf2Items, TotalVadaiSales )
print(f'Total number of Sales in a week is : {TotalSalesOfWeek}')

AvgSalesOfWeek = divideAFromB ( TotalSalesOfWeek , NoOfDaysPerWeek )
print(f"Your Total Average in a week is : {AvgSalesOfWeek}")

TotalSalesOfMonth = multiplyTwoNumbers ( TotalSalesOfWeek , NoOfWeekPerMonth)
print(f'Your Total Sales in a Month is : {TotalSalesOfMonth}')

#calculate profit.
for CoffeeProit in coffeeSales:
    ProfitOFCoffee = multiplyTwoNumbers(costOfCoffee , CoffeeProit)
print(f"Your Total Profit in Coffee is : {ProfitOFCoffee}")

for TeaProfit in teaSales:
    ProfitOfTea = multiplyTwoNumbers( costOfTea , TeaProfit )
print(f'Your Total Profit in Tea is : {ProfitOfTea}')

for VadaiProfit in vadaiSales:
    ProfitOfVadai = multiplyTwoNumbers ( costOfVadai , VadaiProfit )
print(f'Your Total profit in vadai is : {ProfitOfVadai}')

#Call divide function to get the average from all three subjects
TotalProfitOf2Items = addTwoNumbers ( ProfitOFCoffee , ProfitOfTea )
TotalProfitOfSales = addTwoNumbers ( ProfitOfVadai , TotalProfitOf2Items )
print(f"Your Total profit in all three item is : {TotalProfitOfSales}")

avg = divideAFromB ( TotalProfitOfSales , NoOfItems)
print(f"Your Average profit in all three items is : {avg}")

'''
Output:

Total sales of coffee in a week is : 548
Total sales of tea in a week is : 1770
Total sales of vadai in a week is : 446
Total number of Sales in a week is : 2764
Your Total Average in a week is : 394.85714285714283
Your Total Sales in a Month is : 11056
Your Total Profit in Coffee is : 3000
Your Total Profit in Tea is : 6920
Your Total profit in vadai is : 3000
Your Total profit in all three item is : 12920
Your Average profit in all three items is : 4306.666666666667

'''