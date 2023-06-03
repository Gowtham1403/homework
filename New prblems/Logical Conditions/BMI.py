############ Problem 2 ####
#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input.

'''
If your BMI is less than 18.5, it falls within the underweight range.
If your BMI is 18.5 to 24.9, it falls within the Healthy Weight range.
If your BMI is 25.0 to 29.9, it falls within the overweight range.
If your BMI is 30.0 or higher, it falls within the obese range.
'''

weight=int(input("Enter the weight of the person in kg: "))
height=float(input("enter the height of the person in meters: "))
bmi=(weight)/(height**2)
print(f"The body mass index of the person is : {bmi}")
if bmi < 18.5:
    print("the person is underweight")
elif bmi >= 18.5 and bmi < 25:
    print("the person is normal weight")
elif bmi >= 25 and bmi < 30:
    print("the person is overweight")
else:
    print("the person is obesity")

