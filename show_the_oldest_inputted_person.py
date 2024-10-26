name = []
age = []
oldest_user = {}                                                # purpose: show the name of oldest
                                                                # bugs: cant save for multiple same age
while True:                                                     # loop1 procs the program to end+show oldest or redo
    while True:                                                 # loop2 asks for re input
        while True:                                             # loop3 asks for input and check error and invalid
            try:
                name.append(input('Input your name: '))
                age.append(int(input('Input your age: ')))
            except:
                print('Your inputted data has caused an error')
            
            if name[0].isalpha() == True and age[0] > 0 == True:       # check if data is valid
                try:
                    if name[1] in name and age[1] in age:                                           # asks if 2nd index exist
                        if age[0] > age[1]:                                                         # if 2nd index exist, compares if bigger or not
                            name.pop(-2)                                                            # put in dic if bigger
                            age.pop(-2)
                        if age[0] == age[1]:
                            oldest_user = dict(zip(name, age))
                        if age[0] < age[1]:
                            oldest_user = dict(zip(name, age))
                            name.pop(-1)
                            age.pop(-1) 
                except:
                    oldest_user = dict(zip(name, age))
                break                                           # break loop3
            else:
                print('\nERROR. Inputted data is removed. Please input valid data.\n')
                name.pop(-1)                                    # removes invalid but no error
                age.pop(-1)
            
        input_again = input('Do you want to input another user? Y/N\n')
        break                                                   # break loop2
    
    if input_again == "N" or 'n':
        print(oldest_user)
        break                                                   # break loop1
    elif input_again != 'Y' or 'y':
        print('Invalid input')