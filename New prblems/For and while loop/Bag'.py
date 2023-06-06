########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold


#initialize variables
redBags, greenBags = 100, 200
totalSales=0 
totalBagsSold = 0

while (totalSales < 10000 or totalBagsSold < 10) :
    NoOfRedBags = int(input("Enter the number of red color bag that purchased by customers : "))
    NoOfGreenBags = int(input("Enter the number of green color bags that purchased by customers: "))

    TotalCost = (NoOfGreenBags*greenBags) + (NoOfRedBags*redBags)
    
    totalSales += TotalCost
    
    print(totalSales)
 
    BagSold = NoOfGreenBags + NoOfRedBags
    totalBagsSold += BagSold
    print(totalBagsSold)

print (f"Total number of sales is : {totalSales} and number of bag sold is : {totalBagsSold}")  
