from art import logo
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first Number? :"))

    for i in operations:
        print(i)

    should_continue = True

    while(should_continue):
        op = input("Pick an operation: ")
        num2 = float(input("What's the next Number? :"))
        ans = operations[op](num1,num2)

        print(f"{num1} {op} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans} or type 'n' to start a new calculation: ").lower()=='y':
            num1 = ans
        else:
            should_continue = False
            calculator()     #recursion


calculator()
