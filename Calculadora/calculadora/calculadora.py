import graphics.py





def add(a, b):
    return a + b


def subs(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        print("Can't divide by 0")
        return 0
    else:
        return a / b


while True:
    print("\nSelect operation:")
    print("q. Quit")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice: ")
    
    if choice == 'q':
        print("Thanks for using this calculator. Come back soon.")
        break
    
    if choice in ['1', '2', '3', '4',]:
        num1 =float(input("Enter first number: "))
        num2 =float(input("Enter second number: "))
        
        
        if choice == '1':
            result = add(num1, num2)
            print ("The result is: ", result)


        elif choice == '2':
            result = subs(num1, num2)
            print ("The result is: ", result)
        
            
        elif choice == '3':
            result = mult(num1, num2)
            print ("The result is: ", result)


        elif choice == '4':
            result = div(num1, num2)
            print ("The result is: ", result)
    
    else:
        print("Invalid input")

        