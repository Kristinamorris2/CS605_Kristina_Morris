print("Welcome to the Simple Calculator!")

while True: 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter the operation number: ")

    if choice == "1":
        result = num1 + num2 
        print(f"Result: {num1} + {num2} = {result}")
        
    elif choice == "2":
        result = num1 - num2 
        print(f"Result: {num1} - {num2} = {result}")
        
    elif choice == "3":
        result = num1 * num2 
        print(f"Result: {num1} * {num2} = {result}")
        
    elif choice == "4":
        if num2 == 0:
            print("Undefined")
        else:
            result = num1 / num2 
            print(f"Result: {num1} / {num2} = {result}")
            
    else: 
        print("Invalid Operation")

    again = input("Do you want to perform another calculation? (yes/no):")

    if again == "no":
        print("Goodbye!")
        break
