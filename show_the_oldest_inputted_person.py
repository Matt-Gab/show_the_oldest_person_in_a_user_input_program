coe_1_7 = {}
data_address = 0

# Loop1: used to ask user for next input
while True:
    # Loop2: used to auto-retry when input raised an error
    while True:
        try:
            data_address = data_address + 1
            first_name = input("Pls input first name: ")
            last_name = input("Pls input last name: ")
            

            
            # Loop3: used to retry when number is not 11 characters
            while True:
                age = int(input("Pls input age: "))

                if age > 0 and age < 123:
                    # this is to stop Loop3
                    break

            coe_1_7[data_address] = {
                "first_name" : first_name,
                "last_name" : last_name,
                "age" : age,
            }

            retry = input("Retry? ")
            # this is to stop Loop2
            break
        except:
            print("Ay mali!!!!")

    if retry == "n":
        print(coe_1_7[data_address]["first_name"])
        print(coe_1_7[data_address]["last_name"])
        print(coe_1_7[data_address]["age"])
        
        
        # this is to stop Loop1
        break
    elif retry != "y":
        print("Invalid")