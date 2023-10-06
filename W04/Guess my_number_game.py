import random;
again = True;

while again:
    counter = 0;
    magic_number = random.randint(1, 100);
    guess_number = magic_number + 1;
    print(magic_number);
    while guess_number != magic_number:
        counter += 1;
        guess_number = int(input('What is your guess? '));
        
        if guess_number < magic_number:
            print('Higher');
        elif guess_number > magic_number:
            print('Lower');
        else:
            print('You guessed it!');
            print(f'You took {counter} guesses');
    print('Finished game');
    again = input('Do you want to start again? (YES or NOT)');
    if again.lower() == 'yes':
        again = True;
    else:
        again = False;
