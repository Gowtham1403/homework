PriceOfCoffee = 100
PriceOfVadai = 100
PriceOfSandwich = 200
PriceOfCoke = 60
CoffeeDiscountBill = 0

no_of_coffee = int(input("Enter the number of coffee you want : "))
no_of_Vadai = int(input("Enter the number of vadai you want : "))
no_of_Sandwich = int(input("Enter the number of sandwich you want : "))
no_of_Coke = int(input("Enter the number of coke you want : "))

TotalBill = (no_of_coffee * PriceOfCoffee) + (no_of_Vadai * PriceOfVadai) + (no_of_Sandwich * PriceOfSandwich) + (no_of_Coke * PriceOfCoke)
if no_of_Sandwich >= 1 and no_of_coffee >= 1 and no_of_Vadai :
    if (no_of_Sandwich > 1 or no_of_Vadai >= 2):
        PriceOfCoffee = 50
        TotalBill = TotalBill - PriceOfCoffee
        CoffeeDiscountBill = 1
if (no_of_coffee >= 1 and no_of_Sandwich >= 1 and no_of_Vadai >= 1 and no_of_Coke >= 1):
    TotalBill = ( TotalBill - TotalBill * 0.2 )
if ( TotalBill > 1000 and CoffeeDiscountBill == 0):
    TotalBill = TotalBill - (TotalBill * 0.2)
print(f"Your Total Amount is : {TotalBill}")
print("Thank you visit again !!")