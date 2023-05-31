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
    
'''
Output :

enter the amount you have: 100
PS C:\Users\next\OneDrive\Desktop\Gowtham_Sayur\homework> 

enter the amount you have: 1200
YOU CAN BUY 1 CHOCOLATE   
the balance amount is 1000
YOU CAN BUY 1 CAKE        
the balance amount is 850 
YOU CAN BUY 2 CHOCOLATE   
the balance amount is 650 
YOU CAN BUY 2 CAKE        
the balance amount is 500 
YOU CAN BUY 3 CHOCOLATE
the balance amount is 300
YOU CAN BUY 3 CAKE
the balance amount is 150
YOU CAN BUY 4 CAKE
the balance amount is 0

'''