def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def div (a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f" Cannot divide by 0 you moron, fuck off {e}")
        result = "Are you retarded?"
    return result

def mul (a, b):
    return a * b


d = {"add": add, "sub": sub, "div": div, "mul": mul}



def operation_input():
    ops = d.keys()
    operation = str(input(f"Would you like to?: {', '.join(ops)}")).lower()
    while operation not in ops:
        operation = str(input(f"Would you like to {', '.join(ops)}? ").lower())
    print(f"You choose to perform {operation} operation")
    return operation


def number_input(n = " "):
    try:
        the_num = int(input(f"Please enter your {n} number: "))

    except ValueError:
        print("Oi, retard - this shit must be a number. ")
        the_num = number_input(n)

    return the_num

def number_input_check():
    num1 = number_input("First")
    num2 = number_input("Second")
    return num1, num2


def actual_calc(num1, num2, operation):
    return d[operation](num1,num2)

def monkeyman():
    start = True
    while start:
        num1, num2 = number_input_check()
        op = operation_input()
        print(actual_calc(num1,num2, op))

monkeyman()