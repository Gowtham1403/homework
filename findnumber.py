def find_numbers():
    numbers = []
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            numbers.append(i)
    return numbers
numbers = find_numbers()
print(numbers)