from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        return n1 / n2
    except:
        return "Invalid input!"


# hier wurden functions als values definiert, keine Strings
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    result = 0
    calc_finished = False

    print(logo)

    first_number = int(input("What is the first number?: "))
    for key in operations:
        print(key)
        # print(type(operations[key]))

    while not calc_finished:
        input_op = input("Pick an operation: ")
        second_number = int(input("What is the next number?: "))

        try:
            operation = operations[input_op]
        except:
            print("ERROR: Wrong operation!")
            continue

        result = operation(first_number, second_number)
        print(f"{first_number} {input_op} {second_number} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == "y":
            first_number = result
        else:
            calc_finished = True
            # Recursion
            calculator()


calculator()
