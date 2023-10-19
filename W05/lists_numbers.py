number_list = [];
number = None;
add = 0;
average = 0;
largest = 0;
smallest = 0;

print('Enter a list of numbers, type 0 when finished.');

while number != 0:
    number = int(input('Enter number: '));
    if number != 0:
        number_list.append(number);
    add += number;

    if number > largest:
        largest = number;
    if smallest == 0:
        smallest = largest;
    if  number > 0 and number < smallest:
        smallest = number;


average = add / len(number_list);

print(f'The sum is: {add}');
print(f'The average is: {average}');
print(f'The largest number is: {largest}');
print(f'The smallest positive number is: {smallest}');

print('The sorted list is: ')
sorted_list = sorted(number_list);

for number_item in sorted_list:
    print(number_item);
