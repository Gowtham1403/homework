'''
1. Write an app for a cafe. Decide on the items in the cafe, stock of each item in the morning, 
stock in the evening, sales amount at the end of the day and profit for each item. You need to restock an item 
if the supply reaches 20% of the stock. Print the 3 items with highest sales, and top 3 highest profit.
'''

#PROGRAM :


import time
startTime = time.time()
timeLimit = 30

itemsInCafe = ['coffee','tea','cappucino','cookie']
itemPrice = [40,35,50,30]
itemProfit = [12,10,14,5]
itemStock = [30,30,20,40]
itemStockRefill = [30,30,20,40]
itemSales = [0,0,0,0]
topSale = [0,0,0,0]
topProfit = [0,0,0,0]

quantityInWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityInDigits = ['1','2','3','4','5','6','7','8','9']


def CustomerInput(customerInput):
    
    list1 = list(customerInput.split())
    global quantities 
    quantities = []
    

    for i in range(len(itemsInCafe)) :
        
        if itemsInCafe[i] in list1:
            
            index = (list1.index(itemsInCafe[i])) - 1
            
            for x in range(len(quantityInWords)) :
                
                if quantityInWords[x] in list1[index] or quantityInDigits[x] in list1[index] :
                    
                    quantities.insert(i,int(quantityInDigits[x]))

        else:
            
            quantities.insert(i,0)

      
        itemStock[i] -= quantities[i]
        itemSales[i] += quantities[i]

        
        if itemStock[i] <= (itemStockRefill[i] * 0.2):
        
            itemStock[i] = itemStockRefill[i]
            print(f"{itemsInCafe[i]} Refilled....")
            
def topItemsCategory():

   
    for x in range(len(itemSales)) :
        topSale[x] = itemSales[x]
        topProfit[x] = itemSales[x] * itemProfit[x]
    
    a = tuple(topProfit)

    print("\nTop 3 Sales items")
    
  
    for i in range (6) :

        if i < 3 :

       
            print(f"{i+1} - {max(topSale)} - {itemsInCafe[itemSales.index(max(topSale))]}")
            topSale.remove(max(topSale))
            continue

        elif i == 3 :

            print("\nTop 3 Profit items")

     
        print(f"{i-2} - {max(topProfit)} - {itemsInCafe[a.index(max(topProfit))]}")
        topProfit.remove(max(topProfit))

def main() :

    print("\t...Welcome to the cafe..")
    print("(Here are the items that we can served)")

   
    for item in range(len(itemsInCafe)) :

        print(f"{item+1}. {itemsInCafe[item].upper()}")

  
    while (time.time() - startTime) < timeLimit :    

        customerInput = input("Enter ur order... : ")

        CustomerInput(customerInput.lower())

    topItemsCategory()

    
    for z in range(len(itemsInCafe)) :
            
        itemStock[z] = itemStockRefill[z]
        
    print("All items Refilled....")

main()