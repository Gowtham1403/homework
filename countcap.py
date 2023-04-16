def countCap(string): 
    upperCount = 0
    lowerCount = 0
    
    for char in string:
        if char.isupper():
            upperCount = upperCount + 1
        elif char.islower():
            lowerCount = lowerCount + 1
    return (upperCount, lowerCount)

def main():
    string = input("Enter a String : ")
    result = countCap(string)
    
    print(f'Number of Capital letter in your string = {result[0]}')
    print(f'Number of small letter in your string = {result[1]}')
    
main()