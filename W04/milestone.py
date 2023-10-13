secret_word = 'hello';
counter = 0;
guess = '';

print('Welcome to the word guessing game!');

while guess != secret_word:
    guess = input('What is your guess? ');
    if guess.lower() != secret_word.lower():
        print('Your guess was not correct.');
    counter += 1;

print('Congratulations! You guessed it!')
print(f'It took you {counter} guesses.');