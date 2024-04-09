import math

def calculator():
    print("Welcome to Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Calculate Square Root")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Exiting Calculator. Goodbye!")
        return

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Division by zero!")
    elif choice == '5':
        num = float(input("Enter a number: "))
        if num >= 0:
            print("Result:", math.sqrt(num))
        else:
            print("Error: Cannot calculate square root of a negative number!")
    else:
        print("Invalid input. Please enter a valid choice.")

    calculator()

calculator ()