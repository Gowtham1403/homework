
def palindrome(str):
    if len(str) <= 1:
        return True
 # first and last characters of the string are not same,it is not a palindrome
    if str[0] != str[-1]:
        return False
    return palindrome(str[1:-1])

str = input("Enter the String:" )
if palindrome(str):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")
