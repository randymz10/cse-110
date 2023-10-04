grade = float(input("What's your grade? "));
grade_letter = '';
grade_last_digit = grade % 10;
grade_plus = '';

if(grade_last_digit >= 7):
    grade_plus = '+';
elif(grade_last_digit < 3):
    grade_plus = '-';


if(grade >= 90):
    if(grade_plus == '+'):
        grade_plus = '';
    grade_letter = 'A';
elif (grade < 90 and grade >= 80):
    grade_letter = 'B';
elif (grade < 80 and grade >= 70):
    grade_letter = 'C';
elif (grade < 70 and grade >= 60):
    grade_letter = 'D';
else:
    if(grade_plus != ''):
        grade_plus = '';
    grade_letter = 'F';

print(f'You have {grade_letter}{grade_plus}');

if (grade > 70):
    print('Congratulations!!');
else:
    print('You need to study more');

