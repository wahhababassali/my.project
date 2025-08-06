def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error! Division by zero."
        result /= num
    return result

# Main loop
while True:
    print("\n--- Simple Calculator (Multiple Numbers) ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        user_input = input("Enter numbers separated by spaces: ")
        try:
            numbers = list(map(float, user_input.split()))
            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {add(numbers)}")
        elif choice == '2':
            print(f"Result: {subtract(numbers)}")
        elif choice == '3':
            print(f"Result: {multiply(numbers)}")
        elif choice == '4':
            print(f"Result: {divide(numbers)}")
    else:
        print("Invalid choice! Please try again.")
