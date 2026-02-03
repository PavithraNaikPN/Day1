a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid operation")
       
        
name = input("Enter your name: ")
print("Good Afternoon " + name + "!")

name = print("Pavithra")
age = print("22")

print(f"My name is {name} and I am {age} years old")
