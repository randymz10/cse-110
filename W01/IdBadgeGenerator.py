print('Please enter the following information:')
print()
first_name = input('First name: ')
last_name = input('Last name: ')
email_address = input('Email address: ')
phone_number = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')
hair = input('Hair: ')
eyes = input('Eyes: ')
month = input('Month: ')
training = input('Training (yes/no): ')

print('The ID Card is:')
print('----------------------------------------')
print(last_name.upper() + ', ' + first_name.capitalize())
print(job_title.title())
print('ID: ' + id_number)
print()
print(email_address.lower())
print(phone_number)
print('Hair: ' + hair  + '{: >20}'.format('Eyes: ') + eyes)
print('Month: ' + month + 'Training: '.rjust(20) + training)
print('----------------------------------------')