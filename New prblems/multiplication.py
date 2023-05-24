
######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.


# for loop for 7 to 17
for i in range(7, 17):  
    print(f"Multiplication table of {i}:")
    
# for Loop for 1 to 12
    for j in range(1, 13):  
        result = i * j
        print(f"{i} * {j} = {result}")
    print()  