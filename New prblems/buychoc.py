#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.
#find how many choc and cake the user can buy
PerChocolate=200
PerCake=150
noOfCake = 0
noOfChoc = 0
#get budget
money=int(input("enter the amount you have: "))


while (money >= 150) : 
    if (money > 200) :
        noOfChoc += 1
        print(f"YOU CAN BUY {noOfChoc} CHOCOLATE")
        money -= 200
        print(f"the balance amount is {money}")
        
        
    
    noOfCake+=1
    print(f"YOU CAN BUY {noOfCake} CAKE")
    money-=150
    print(f"the balance amount is {money}")