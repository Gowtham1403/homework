############## Problem  1 #################### 
#Ask first friend the colors they like. Save it in a list
#Ask another friend the same question. If the color is in the first friend's list, 
#Print "You both like "name of the color"
#If it is not in the first friend's list, Save it another list.

favColor1=[]
favColor2=[]
commonColor = []
noOfFavColor1= int(input("enter the number of favourite colors of sree:"))
noOfFavcolor2= int(input("enter the number of favourite colour of aravindhan:"))
for col1 in range(noOfFavColor1):
    color=input("enter your favourite color sree: ")
    favColor1.append(color)
for co12 in range(noOfFavcolor2):
    colors=input("enter your favourite color aravindhan: ")
    if colors not in favColor1:
         favColor2.append(colors)
    else:
        commonColor.append(colors)
            
print(f"favourite colors of sree is {favColor1}")
print(f"favourite colors of aravindhan is {favColor2}")
print(f"you both like the same color, the colors are: {commonColor}")

'''
Output:

enter the number of favourite colors of sree:2
enter the number of favourite colour of aravindhan:3
enter your favourite color sree: red
enter your favourite color sree: blue
enter your favourite color aravindhan: green
enter your favourite color aravindhan: blue
enter your favourite color aravindhan: black
favourite colors of sree is ['red', 'blue']
favourite colors of aravindhan is ['green', 'black']
you both like the same color, the colors are: ['blue']

'''