number = -1;

while number < 0:
    number = int(input('Please type a positive number: '));
    if(number < 0):
        print(f'Sorry, that is a negative number. Please try again.')
print(f'The number is: {number}');