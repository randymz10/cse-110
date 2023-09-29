# Write a program that asks the user for two integers.

# Then, write three separate if/else statements as follows:

# If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

# If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

# If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

first_number = int(input('What is the first number? '));
second_number = int(input('What is the second number? '));

if first_number > second_number:
    print('The first number is greater');
else:
    print('The first number is not greater');

if first_number == second_number:
    print('The numbers are equal');
else:
    print('The numbers are not equal');

if second_number > first_number:
    print('The second number is greater');
else:
    print('The second number is not greater');

print();

favorite_animal = input('What is your favorite animal? ');

if favorite_animal.lower() == 'gato':
    print("That's my favorite animal too!");
else:
    print('That one is not my favorite.');