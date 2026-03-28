print("=== SIMPLE CALCULATOR ===")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
