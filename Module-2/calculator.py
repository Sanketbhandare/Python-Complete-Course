import math_operations

num1 = int(input("Please provide number 1: "))
num2 = int(input("Please provide number 2: "))

choice = int(input("\n 1. Addition \n 2. Substraction \n 3. Division \n 4. Multiplication \n Please provide your input: "))

if choice == 1:
    print("\n Addition is ",math_operations.add(num1, num2))
elif choice == 2:
    print("\n Substraction is ",math_operations.sub(num1, num2))
elif choice == 3:
    print("\n Division is ",math_operations.div(num1, num2))
elif choice == 4:
    print("\n Multiplication is ",math_operations.mul(num1, num2))
else:
    print("\n Invalid Input")