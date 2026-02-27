#Mi participacion taller #1, Registro de participantes.

print("Welcome to Riwi user registration")

people_registered = int(input("How many persons are you going to register?: "))
n=0
while n < people_registered:
    
    print(f"\n--- Registering person #{n + 1} ---")

    name = input("Please enter your full name: ")
    
    try:
        age = int(input("Please enter your age: "))
        if age <=0:
            print("Age not valid")
            continue
    except ValueError:
                print("invalid value")

    acknowledge = int(input("Do you have basic acknowledge developing?\n Yes (1) \n No (2) \n : "))
    print("")

    n+=1 

    if age > 15 and acknowledge == 1:  
        print("---Thanks, welcome to the proyect!---")

    else: 
    
        print("---Sorry, you can not participate---")

print("\nRegistration complete! All users have been stored.")





