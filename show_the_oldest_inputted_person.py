coe_1_7 = {}
                                                         # loop1 ask for the next action (retry)
while True:                                                     # loop2 if an error occurs this will proc
    while True:                                                 # loop3 inputs data and check if correct data + user id
        try:
            while True:
                user_id = user_id + 1
                first_name = input("Pls input first name: ")
                last_name = input("Pls input last name: ")
                age = int(input("Pls input age: "))

                if first_name.isalpha() and last_name.isalpha() and age > 0 and age < 123:
                    break                                               # checks if input data is correct
        
            coe_1_7[user_id] = {
                "first_name" : first_name,
                "last_name" : last_name,
                "age" : age,
            }

            retry = input("Retry? Y/N ")
            break                                                   # break loop3 and goes to loop1
        except:
            print("redo")
            
    if retry == "N" or "n":
        for i in range (user_id):                                   # loop4 finds the oldest
            print('placeholder')
        break                                                       # break loop1 and end program
    elif retry != "Y" or "y":
        print("Invalid answer")                                     # loop1 will proc