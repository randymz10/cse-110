option = None;
item = None;
index_item = -1;
price = 0;
total_price = 0;
cart = [];
prices = [];


print('Welcome to the Shopping Cart Program!');

while option != 5:
    
    print('\nPlease select one of the following:');
    print('1. Add item');
    print('2. View cart');
    print('3. Remove item');
    print('4. Compute total');
    print('5. Quit');
    
    option = int(input('\nPlease enter an action: '));
    
    if option == 1:
        item = input('What item would you like to add? ');
        price = float(input(f"What is the price of '{item}'? "));
        cart.append(item);
        prices.append(price);
        print(f"'{item}' has been added to the cart.");
    if option == 2:
        print('The contents of the shopping cart are:');
        for i, cart_item in enumerate(cart):
            print(f'{i + 1}. {cart[i]} - ${prices[i]}');
    if option == 3:
        index_item = int(input('Which item would you like to remove? '));

        cart.pop(index_item);
        prices.pop(index_item);
        print('Item removed.');
    if option == 4:
        for price_item in prices:
            total_price += price_item;
        print(f'The total price of the items in the shopping cart is ${total_price:.2f}');
    
    total_price = 0;
    
    if option == 5:
        print('Thank you. Goodbye.');