name = []
age = []


while True:
    while True:
        while True:                                             # loop2 input and check if error
            try:
                name.append(input('Input your username: '))
                age.append(int(input('Input your age: ')))
                
                if name.isalpha() and age > 0 and age < 123:    # statements check if correct or bigger than the last
                    if name[1] in name and age[1] in age:
                        if age[0] > age[1]:
                            oldest_user = dict(zip(name, age))
                            name.remove(name[ : -2])
                            age.remove(age[ : -2])
                        if age[0] == age[1]:
                            oldest_user = dict(zip(name, age))
                        if age[0] < age[1]:
                            oldest_user = dict(zip(name, age))
                            name.remove(name[ : -1])
                            age.remove(age[ : -1]) 
                    else:
                        oldest_user = dict(zip(name, age))
                    break
                else:
                    print('Inputted data is remove. Please input valid data.\n')  # removes invalid enter
                    name.remove(name[ : -1])
                    age.remove(age[ : -1])
                    
            except:
                print('Your inputted data has caused an error')
            
        input_again = input('Do you want to input another user? Y/N')
        break
    
    if input_again == "N" or 'n':
        print(oldest_user)
    elif input_again != 'Y' or 'y':
        print('Invalid input')