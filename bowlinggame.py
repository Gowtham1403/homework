'''
total number of frames = 10
each frame we have 2 rolls 
user have to bowl 
if 10th frame is strike or spare 

'''

frame = 1
FirstRoll = 0
SecondRoll = 0
total = 0
perFramePoint = 0
numberofpins = 10

while frame < 11 :
    print(f"Frame number is :{frame}")
    FirstRoll = int(input("Enter the First roll value on or below 10: "))
    if FirstRoll == 10:
        print(f"Your first roll value is : {FirstRoll}")
    else:
        SecondRoll = int(input("Enter the Second roll value on or below 10:"))
        print(f"your second roll value is : {SecondRoll}")
    perFramePoint = FirstRoll + SecondRoll
    print(f"Your Frame total is : {perFramePoint}")
    total = total +  (FirstRoll + SecondRoll)
    print(f"Your Overall total is : {total}")
    frame = frame + 1
    
