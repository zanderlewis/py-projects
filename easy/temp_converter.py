# Difficulty: III

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return 9.0/5.0 * celsius + 32

while True:
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 3:
        break

    temp = float(input("Enter temperature to convert: "))

    if choice == 1:
        print("Result: ", fahrenheit_to_celsius(temp))
    elif choice == 2:
        print("Result: ", celsius_to_fahrenheit(temp))
    else:
        print("Invalid choice, please choose a number between 1 and 3.")