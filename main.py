'''
This code is an implementation of calculator for Reverse Polish Notation (RPL)
'''


def calculate_rpn(expression):
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y

    # Initialise the operators dictionary
    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    # Initialise a stack list to store operands and intermediate results
    stack = []

    # Split string into tokens separated by spaces and iterate over each token
    for token in expression.split():

        # Check if the current token is an operator dictionary
        if token in operators:

            # Pop the top two elements from the stack, 'y' is the last pushed element, 'x' is the second last
            x = stack.pop()
            y = stack.pop()

            # Use the operator from the dictionary to apply the function on x and y storing the result
            result = operators[token](x, y)
            stack.append(result)
        else:
            stack.append(float(token))

            # Return the top element of the stack as the final result, or None if the stack is empty
            return stack[0] if stack else None


if __name__ == "__main__":
    expression = input("Enter the expression: ")
    result = calculate_rpn(expression)
    print(result)
