def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero is not allowed."

def square(x):
    return x*x
    

def calculator():
    print("Welcome to a calculator Ronnie Harrod created!")
    print("Please select an operation:")
    print("1. Additon")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")


        if choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter fist number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} squared = {square(num1)}")
        else:
            print("Invalid choice. Please enter a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Exiting the calculator.")
            break

calculator()
