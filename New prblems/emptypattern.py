


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

for row in range(length):
    temp = ''
    for col in range(width):
        if row == 0 or row == length - 1 or col == 0 or col == width - 1:
              
            temp += '*'
            continue
        temp += ' '
    print(temp)
        
