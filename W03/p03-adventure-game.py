print('Welcome to Adventure Game');
print();
first_choice = input('You are walking through a forest and you find two paths: on the RIGHT you see a mountain and on the LEFT you see a beach. Which path do you choose? ');

while first_choice != 'right' or first_choice !='left':
    if first_choice.lower() == 'right':
        second_choice = input('You continue walking and a black panther appears. Do you RUN, do you continue WALKING as if nothing happened or do you HIDE behind a tree to wait for the panther to leave? ');
        
        while second_choice != 'run' or second_choice != 'walking' or second_choice != 'hide':
            if second_choice.lower() == 'run':
                third_choice = input('While running you come across a waterfall 30 meters high you see that BELOW the waterfall falls towards a lake and ABOVE a helicopter is passing by, do you: do you jump into the lake or ask the helicopter for help? ')
            elif second_choice == 'walking':
                third_choice = input('');
            elif second_choice == 'hide':
                third_choice = input('');
            else:
                third_choice = input('Please, digit RUN, WALKING or HIDE ');

    elif first_choice.lower() == 'left':
        second_choice = input('');
    else :
        first_choice = input('Please, digit RIGHT or LEFT ');