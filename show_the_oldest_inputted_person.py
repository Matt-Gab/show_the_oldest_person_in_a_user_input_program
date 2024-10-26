
name = []
age = []


while True:
    while True:
        while True:                                                     # loop2 input and check if error
            try:
                name.append(input('Input your username: '))
                age.append(int(input('Input your age: ')))
                if name.isalpha() and age > 0 and age < 123:
                    if 
                        oldest_user = dict(zip(name, age))
                    break
                else:
                    print('Inputted data is remove. Please input valid data.')
                    user_id_list = user_id_list[ : -1]                   # removes no error invalid enter
                    name = name[ : -1]
                    age = age[ : -1]
                    
            except:
                print('Your inputted data has caused an error')
            
        input_again = input('Do you want to input another user? Y/N')
        break
    
    if input_again == "N" or 'n':
        print('hello / placeholder')
    elif input_again != 'Y' or 'y':
        print('Invalid input')