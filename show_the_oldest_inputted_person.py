name = []                                                       # known bugs: cant save for multiple same age and name
age = []                                                        # purpose: show the name of oldest
                                                                
while True:                                                     # loop1 procs the program to end+show oldest or redo
    while True:                                                 # loop2 asks for re input
        while True:                                             # loop3 asks for input and check error and invalid
            try:
                name.append(input('Input your name. Alphabet only\n'))
                age.append(int(input('Input your age. Integers only\n')))
            except:
                print('Your inputted data has caused an error')
            
            if name[0].isalpha() == True and age[0] > 0 and age[0] < 123:       # check if data is valid
                try:
                    if name[1] in name and age[1] in age:                       # asks if 2nd index exist
                        if age[0] > age[-1]:                                    # if 2nd index exist, compares if bigger or not
                            name.pop(-1)
                            age.pop(-1)
                        if age[0] < age[-1]:
                            name.pop(-2)
                            age.pop(-2)
                except:
                    break                                       # break loop3 too
                break                                           # break loop3
            else:
                print('\nERROR. Inputted data is removed. Please input valid data.\n')
                name.pop(-1)                                    # removes data invalid but no error
                age.pop(-1)
            
        input_again = input('Do you want to input another user? Y/N\n')
        break                                                   # break loop2
    
    if input_again == "N":
        print('The oldest are')
        for i in range(len(name)):
            print(name[i], age[i])
        break                                                   # break loop1
    elif input_again != 'Y':
        print('Invalid input')