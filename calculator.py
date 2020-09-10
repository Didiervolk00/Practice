#The operations the calculator is able to do
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    return x / y

#Request for user input, choose the operation
print("Select operation")
print("Add (1)")
print("Substract (2)")
print("Multiply (3)")
print("Devide (4)")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    
    #Request for calculator input
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        #Convert the two numbers
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")