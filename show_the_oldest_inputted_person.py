user_added_name_age = {}

while True:                                                 # loop that checks if the user wants to input another person + age
    while True:                                             # loop that checks if inputted data will result to an error
        try:
            first_name = input('Enter your first name\n')
            last_name = input('Enter your surname\n')
            age = int(input('Enter your age\n'))  
                                                 # loops that checks if inputted data is valid
            if age > 123 and age < 0:
                print('User entered an unnaceptable age')
                break
            if not first_name.isalpha():
                print('User entered an unnaceptable first name')
                break
            if not last_name.isalpha():
                print('User entered an unnaceptable surname')
                break
                
            user_added_name_age[last_name][first_name] = {
                'age' : age    
            }
            
            print(user_added_name_age[last_name][first_name]['age'])
            
            retry = input('Add another user? Y/N\n')
            
        except:
            print('The user has inputted wrong data')
            
    if retry == 'N':
        break
    elif retry != 'Y':
        ('The user has inputted wrong data')