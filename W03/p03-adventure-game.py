# Added loops in ordeer to handled the incorrect inputs
# Added boolean operators


is_finished = False;
print('Welcome to Adventure Game');
print();
first_choice = input('You are walking through a forest and you find two paths: on the RIGHT you see a mountain and on the LEFT you see a beach. Which path do you choose? ');

while (first_choice != 'right' or first_choice !='left') and is_finished == False:
    if first_choice.lower() == 'right':
        second_choice = input('You continue walking and a black panther appears. Do you RUN, do you continue WALKING as if nothing happened or do you HIDE behind a tree to wait for the panther to leave? ');
        
        while (second_choice.lower() != 'run' or second_choice.lower() != 'walking' or second_choice.lower() != 'hide') and is_finished == False:
            if second_choice.lower() == 'run':
                third_choice = input('While running you come across a waterfall 30 meters high you see that BELOW the waterfall falls towards a lake and ABOVE a helicopter is passing by, do you: do you jump into the lake or ask the helicopter for help? ');
                
                while (third_choice.lower() != 'below' or third_choice.lower() != 'above') and is_finished == False:
                    if third_choice.lower() == 'below':
                        print('You fell into the water and, Oh! A treasure!');
                        is_finished = True;
                    elif third_choice.lower() == 'above':
                        print('The helicopter has rescued you');
                        is_finished = True;
                    else:
                        third_choice = input('Please, digit BELOW or ABOVE ');
            
            elif second_choice == 'walking':
                print('Game over, the panther killed you.');
                is_finished = True
            elif second_choice == 'hide':
                third_choice = input('Pass the panther and you are out of danger, you continue your path and you see a dark cave and there is a flashlight next to it. Do you take the FLASHLIGHT and go into the cave or CONTINUE on your way? ');
                
                while (third_choice.lower() != 'flashlight' or third_choice.lower() != 'continue') and is_finished == False :
                    if third_choice.lower() == 'flashlight':
                        print('You take the flashlight and you go into the cave, you walk and, what is that? Oh! a treasure! You have found a treasure!');
                        is_finished = True;
                    elif third_choice.lower() == 'continue':
                        print('You continue your way, you arrive at a town and you meet the love of your life.');
                        is_finished = True;
                    else:
                        third_choice = input('Please, digit FLASHLIGHT or CONTINUE ');
            else:
                second_choice = input('Please, digit RUN, WALKING or HIDE ');
    elif first_choice.lower() == 'left':
        second_choice = input('You see a pirate ship in the distance, you CALL their attention in the distance to go on an adventure with them or you HIDE in fear of being kidnapped by pirates. ');
        
        while (second_choice.lower() != 'call' or second_choice != 'hide') and is_finished == False:
            if second_choice.lower() == 'call':
                third_choice = input('They recruit you as a crew member and you go on a trip with the pirates, while they are sailing you see an island in the distance, do you NOTIFY the captain to go to the island or do you stay QUIET to continue the trip? ');
                while (third_choice.lower() != 'notify' or third_choice.lower() != 'quiet') and is_finished == False:
                    if third_choice.lower() == 'notify':
                        print('They disembark on the island and to their surprise they arrive at an island of gold!');
                        is_finished = True;
                    elif third_choice.lower() == 'quiet':
                        print('The ship is lost and shipwrecked at sea.');
                        is_finished = True;
                    else:
                        third_choice = input('Please, digit NOTIFY or QUIET ')
            elif second_choice.lower() == 'hide':
                third_choice = input('The pirates pass by and you stay on the beach, you see that there is an abandoned ship with several skulls inside, you decide to CHECK the ship or CONTINUE on your way. ');
                while (third_choice.lower() != 'check' or third_choice.lower() != 'continue') and is_finished == False:
                    if third_choice.lower() == 'check':
                        print('You go in to check the abandoned ship and when you go down to the basement, to your surprise you find a pirate treasure!');
                        is_finished = True;
                    elif third_choice.lower() == 'continue':
                        print('You meet your best friend');
                        is_finished = True;
                    else:
                        third_choice = input('Please, digit CHECK or CONTINUE ')
                        
            else:
                second_choice = input('Please, digit CALL or HIDE ');
    else :
        first_choice = input('Please, digit RIGHT or LEFT ');

print('Game finished');

