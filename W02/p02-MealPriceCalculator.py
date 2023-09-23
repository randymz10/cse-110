# Added the price drink for child and adult.
# Done the compute of the drinks in the subtotal.

price_child_meal = float(input("What is the price of a child's meal? "));
price_child_drink = float(input("What is the price of a child's drink? "));
price_adult_meal = float(input("What is the price of an adult's meal? "));
price_adult_drink = float(input("What is the price of a adult's drink? "));
children_quantity = int(input('How many children are there? '));
adults_quantity = int(input('How many adults are there? '));

subtotal = ((price_child_meal + price_child_drink) * children_quantity) + ((price_adult_meal + price_adult_drink) * adults_quantity);

print(f'\nSubtotal: ${subtotal:.2f}\n');

tax_rate = float(input('What is the sales tax rate? '));

sales_tax = (subtotal * tax_rate) / 100;
total = subtotal + sales_tax;

print(f'Sales Tax: ${sales_tax:.2f}');
print(f'Total: ${total:.2f}');

payment_amount = float(input('What is the payment amount? '));

change = payment_amount - total;
print(f'Change: ${change:.2f}');