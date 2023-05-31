

#create a list 
nameList = []
ageList =  []
heightlist=[]
weightlist=[]

#get the input from user and append in list
noOfPeople = int (input("How many people in the family: "))
for member in range (1, noOfPeople + 1):
    name = input("Enter the family member name: ")
    age = input("Eneter the family member age: ")
    height =input("Eneter the family member height: ")
    weight = input("Eneter the family member weight: ")
    nameList.append(name)
    ageList.append(age)
    heightlist.append(height)
    weightlist.append(weight)

#for output
print("\nName\t\tAge\tHeight\t\tWeight")
#in for loop we take namelist in that we add age,height and list
for i, name in enumerate(nameList):
    print(f"{name}\t\t{ageList[i]}\t{heightlist[i]}\t\t{weightlist[i]}")
    
    
'''
Output:

How many people in the family: 2
Enter the family member name: sree
Eneter the family member age: 18
Eneter the family member height: 6
Eneter the family member weight: 55
Enter the family member name: ragu
Eneter the family member age: 19
Eneter the family member height: 5
Eneter the family member weight: 45

Name            Age     Height  Weight
sree            18      6               55
ragu            19      5               45
'''