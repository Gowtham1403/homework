fruit = ["apple","strawberry","banana","orange","kiwi"]
sales = [5,2,13,4,2]
fruitlist = (list(enumerate(fruit)))
Saleslist = (list(enumerate(sales)))
print(fruitlist)
sortedlist = sorted(Saleslist,key=lambda x:x[1],reverse=False)
print(sortedlist)
for i in sortedlist[0:3]:
    print(fruit[i[0]])