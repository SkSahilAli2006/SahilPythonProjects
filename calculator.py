print("Simple Calculator")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = int(input("Apna choice enter karo (1-4): "))

a = float(input("Pehla number: "))
b = float(input("Dusra number: "))

if choice == 1:
    print("Result =", a + b)
elif choice == 2:
    print("Result =", a - b)
elif choice == 3:
    print("Result =", a * b)
elif choice == 4:
    if b != 0:
        print("Result =", a / b)
    else:
        print("Division by zero allowed nahi hai")
else:
    print("Galat choice ❌")
