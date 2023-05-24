############## Problem 2 ####################
#Ask the user how many members in the family. Get Name, age and height and weight.
#add the details into four lists.
#Print the each memeber of the family and their details
#eg output 
# Name      Age     Height(cm)      Weight(kg)
# Ram       35      180             80
# Seetha    34      145             58

nameList = []
ageList = []
heightlist=[]
weightlist=[]
noOfPeople = int (input("How many people in the family"))
for member in range (1, noOfPeople + 1):
    details = input(f"Enter the details of member {member} Name, age, height, weight")
    details.split()
    
print ("Name\t\tAge\t\tHeight(cm)\t\tWeight(kg)") 
for index, member in enumerate(nameList): 
    print( f"{member}\t\t FillinMissingCode to print the details from other lists")