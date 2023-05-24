######## Problem  3 ###############
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. You can use "B" to print black squares

for i in range (8):
    temp = ''
    
    for j in range (8):
        if (i+j) % 2 == 0 :
            
            temp += 'b'
            continue
        
        temp += '\u25A0'
    print(temp)
        