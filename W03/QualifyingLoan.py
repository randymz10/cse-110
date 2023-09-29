loan_size = int(input('How large is the loan? (1-10) '));
credit_history = int(input('How good is your credit history? (1-10) '));
income = int(input('How high is your income? (1-10) '));
down_payment = int(input('How large is your down payment? (1-10) '));
decision = '';

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        decision = 'Yes';
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            decision = 'Yes';
        else:
            decision = 'No';
    else:
        decision = 'No';
else:
    if credit_history < 4:
        decision = 'No';
    else:
        if income >= 7 or down_payment >= 7:
            decision = 'Yes';
        elif income>= 4 and down_payment >= 4:
            decision = 'Yes';
        else:
            decision = 'No';

print(f'Desicion: {decision}');


