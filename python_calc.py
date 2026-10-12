while True:
    print("This is improves calculator")
    num1 = int(input("Enter num#1: "))
    num2 = int(input("Enter num#2: "))
    func = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Check Even/Odd\n6. Calculate Percentage\n7. Exit\n"))
    
    if func == 1:
        print("Addition:", num1 + num2)
    elif func == 2:
        print("Subtraction:", num1 - num2)
    elif func == 3:
        print("Multiplication:", num1 * num2)
    elif func == 4:
        if num2 == 0:
            print("Division by zero is not allowed")
        else:
            print("Division:", num1 / num2)
    elif func == 5:
        if num1 % 2 == 0 and num2 % 2 == 0:
            print("Both numbers are even")
        elif num1 % 2 == 0 and num2 % 2 != 0:
            print("num#1 is even and num#2 is odd")
        elif num1 % 2 != 0 and num2 % 2 == 0:
            print("num#2 is even and num#1 is odd")
        else:
            print("Both are odd")
    elif func == 6:
        if num2 == 0:
            print("Division by zero is not allowed")
        else:
            print("Percentage:", (num1 / num2) * 100)
    elif func == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
