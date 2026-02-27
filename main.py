#Mi participacion taller #1, Registro de participantes.

print("Welcome to Riwi user registration")

people_registered = int(input("How many persons are you going to register?: "))
n=0
while n < people_registered:
    
    print(f"\n--- Registering person #{n + 1} ---")

    name = str(input("Please enter your full name: "))

    age = int(input("Please enter your age: "))

    acknowledge = int(input("Do you have basic acknowledge developing?\n Yes (1) \n No (2) \n : "))

    n+=1 

print("\nRegistration complete! All users have been stored.")




