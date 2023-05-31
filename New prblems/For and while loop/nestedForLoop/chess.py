######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

#for loop begins for column
for i in range (8):
#add a empty string to a new variable
    temp = ''
    
#for loop begins for row   
    for j in range (8):
#if cond for chck even numbers
        if (i+j) % 2 == 0 :
    #if the num is even we add 'b' to empty variable
            temp += 'b'
            continue
    # continue that add white on that empty variable
        temp +='\u25A0'
    # finaly print temp
    print(temp)
        
        
'''
Output:

b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b
b■b■b■b■
■b■b■b■b

'''