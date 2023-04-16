quantityWords = ['one','two','three','four','five','six','seven','eight','nine']
quantityDigits = ['1','2','3','4','5','6','7','8','9']

customer = 1
MaxCustomer = 10

items = {
    'coffee' : 
    {
        'name' : 'coffee',
        'price' : 20,
        'stock' : 20,
        'refill' : 20,
        'profit' : 8,
        'sales' : 0
    },
    'tea' : 
    {
        'name' : 'tea',
        'price' : 25,
        'stock' : 35,
        'refill' : 35,
        'profit' : 10,
        'sales' : 0
    },
    'sandwich' : 
    {
        'name' : 'sandwich',
        'price' : 45,
        'stock' : 25,
        'refill' : 25,
        'profit' : 18,
        'sales' : 0
    },
    'cookies' : 
    {
        'name' : 'cookies',
        'price' : 30,
        'stock' : 30,
        'refill' : 30,
        'profit' : 5,
        'sales' : 0
    }
}

def itemrefill(item):
    if items[item]['stock'] <= items[item]['refill']*0.2:
        items[item]['stock'] =  items[item]['refill']

def processInput(customerInput):
    list1 = list(customerInput.split())
    global quantity,item
    for i in items:
        x = items.get(i)
        if i in list1:
            item = i
            index = (list1.index(i)) - 1 
            for k in range(len(quantityWords)):
                if quantityWords[k] in list1[index] or quantityDigits[k] in list1[index]:
                    quantity = int(quantityDigits[k])
            itemrefill(item)
            x['stock'] -= quantity
            x['sales'] += quantity

def main():
    print("MENU")
    for i,j in items.items():
        print(i.upper())
    while customer <= MaxCustomer:
        customer += 1
        customerInput = input("Enter ur order: ")
        processInput(customerInput.lower())
    #topProfitSales()

main()