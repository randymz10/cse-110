secret_word = 'hola';
counter = 0;
guess = '';
isPresent = False;

print('Welcome to the word guessing game!');

print('Yout hint is: ', end='');

for letter in secret_word:
    print('_ ', end='');


while guess != secret_word:
    guess = input('\nWhat is your guess? ');

    if len(guess) == len(secret_word):
        print('Yout hint is: ', end='');
        for i, letter in enumerate(guess):             
            for letterSecret in secret_word:
                if letter.lower() == letterSecret.lower():
                     isPresent = True;
                     
            if isPresent == False:
                 print('_', end='');
            if isPresent and guess[i] != secret_word[i]:
                    print(f'{guess[i].lower()}', end='');
            if isPresent and guess[i] == secret_word[i]:
                print(f'{guess[i].upper()}', end='');
    else:
        print('Sorry, the guess must have the same number of letters as the secret word');            
    counter += 1;
    isPresent = False;


print('\nCongratulations! You guessed it!')
print(f'It took you {counter} guesses.');